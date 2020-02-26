from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from fns.forms.input_form import InputForm
from fns.forms.search_form import SearchForm
from fns.forms.login_form import LoginForm
from fns.forms.get_ordering_form import GetOrderingForm
from lxml import etree
from xml.etree.cElementTree import tostring
from django.urls import reverse
from fns.models import СвЮЛ, Документ
from django.contrib.postgres.search import SearchVector, SearchQuery
import re
from bokeh.embed import components
from fns.graphs.tegminated import TerminatedGraph
from fns.graphs.terminatedInYear import TerminatedInYearGraph
from fns.graphs.dublicated import DublicatedGraph
from fns.graphs.registeredInYear import RegisteredInYearGraph
import os
import pandas as pd
import datetime
from fns.utils import check_ogrn, check_inn, xslt_process
from rest_framework.renderers import JSONRenderer
from fns.models import ДокументSerializer
import json

from celeryApp.tasks import createXML, newCreateXML, signXML, sendFirstRequest, sendRequest


NUM_ON_PAGE = 25


class egrulView(TemplateView):

    errors = {"not_found": "Отсутсвуют сведения для заданных параметров поиска. ",
              "bad_params": "Неверно заданы параметры поиска. ",
              "multi_result": "Найдено несколько записей, удовлетворяющих заданным параметрам. ",
              "internal_err": "Внутренняя ошибка сервера. ",
              }

    methods_name = {'fo': 'SendFullULRequest',}

    def post(self, request, *args, **kwargs):
        errors = []
        content = ''
        html_egrul = ''
        doc = ''
        search_param = {}
        go_to_search = False
        print('in post egrulView')
        # xml_data = "one.xml"
        # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        xsl_data = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ "/../xsl/one.xsl"
        if not request.is_ajax():
            print('not Ajax')
            return HttpResponseBadRequest('Expected an XMLHttpRequest')
        in_data = json.loads(request.body.decode('utf-8'))
        form = InputForm(data=in_data)
        if 'search' in in_data:
            form.is_valid = True
            param = in_data['search']
            if check_ogrn(param):
                print("param is OGRN", param)
                try:
                    doc = Документ.objects.get(СвЮЛ__ОГРН=param)
                except:
                    errors.append(self.errors["not_found"])
                    return HttpResponseBadRequest('Doc not found')
            # print(xslt_process(doc.СвЮЛ_XML, xsl_data).decode('utf-8'))
            elif check_inn(param):
                print("param is INN")
                try:
                    doc = Документ.objects.get(СвЮЛ__ИНН=param)
                except:
                    errors.append(self.errors["not_found"])
                    return HttpResponseBadRequest('Doc not found')
            else:
                print("param is not INN or OGRN", form.is_valid)
                docs = Документ.objects.filter(СвЮЛ__СвНаимЮЛ__search_vector=SearchQuery(param, config='russian'))
                if docs.count() > 1:         # найдено несколько записей
                    # go_to_search = True
                    # search_param['search'] = param
                    errors.append(self.errors["multi_result"])
                elif docs.count() < 1:
                    errors.append(self.errors["not_found"])
                else:
                    doc = docs[0]
                #   for item in docs:
                #       print(item.СвЮЛ.ОГРН, ' - ', item.СвЮЛ.СвНаимЮЛ.НаимЮЛПолн)
                #       search_result.append(item.get_info())
                # return reverse('search')
                #errors.append(self.errors["not_found"])
            if doc:
                content = doc.get_content()
                html_egrul = xslt_process(doc.СвЮЛ_XML, xsl_data).decode('utf-8')
            response_data = {'errors': form.errors, 'search': in_data['search'], 'content': content,
                             'html_egrul': html_egrul, 'find_errors': errors, 'id': doc.ИдДок,
                             'goToSearch': go_to_search}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        # bound_contact_form = CheckoutForm(data={'subject': in_data.get('subject')})
        # now validate ‘bound_contact_form’ and use it as in normal Django
        else:
            print('in error')
            errors.append(self.errors["not_found"])
            response_data = {'errors': form.errors, 'find_errors': errors}
            return HttpResponse(json.dumps(response_data), content_type="application/json")

    def put(self, request, *args, **kwargs):
        print('in put egrulView')
        errors = []
        if not request.user.is_authenticated:
            print('not authenticated user')
            errors.append("Отправка запросов возможна только для авторизированных пользователей. Пожалуйста, авторизуруйтесь или зарегистрируйтесь в системе")
            response_data = {'errors': {'__all__': errors}}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        user_id = request.user.id
        if not request.is_ajax():
            print('not Ajax')
            return HttpResponseBadRequest('Expected an XMLHttpRequest')
        in_data = json.loads(request.body.decode('utf-8'))
        form = GetOrderingForm(data=in_data)
        if form.is_valid():
            ogrn = in_data['search']
            type = in_data['type']
            if type not in self.methods_name:
                print('unsupported type request ')
                return HttpResponseBadRequest('Expected an XMLHttpRequest')
            try:
                order = (newCreateXML.s({'ogrn': ogrn, 'name':  self.methods_name.get(type), 'user': user_id}, ) | signXML.s() | sendFirstRequest.s() | newCreateXML.s() | signXML.s() | sendRequest.s())()
                # print(order)
            except:
                errors.append(
                    "Ошибка постановки в очередь запросов. Обратитесь пожалуйста к системному администратору")
                response_data = {'errors': {'__all__': errors}}
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        response_data = {'errors': form.errors, 'task_id': order.task_id}
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    def get_context_data(self, **kwargs):
        print('in pget_context')
        context = super(egrulView, self).get_context_data(**kwargs)
        context.update(form=InputForm(), getform=GetOrderingForm())
        return context


class dashboardView(TemplateView):

    def get_context_data(self, **kwargs):
        print('in pget_context dashboardView')
        context = super(dashboardView, self).get_context_data(**kwargs)
        g1 = TerminatedGraph(width=300, height=300)
        p1 = g1.get_graph()
        g2 = TerminatedInYearGraph(width=300, height=300)
        p2 = g2.get_graph()
        g3 = DublicatedGraph(width=300, height=300, N=300)
        p3 = g3.get_graph()
        g4 = RegisteredInYearGraph(width=300, height=300)
        p4 = g4.get_graph()
        script1, div1 = components(p1)
        script2, div2 = components(p2)
        script3, div3 = components(p3)
        script4, div4 = components(p4)
        figures = []
        figures.append({'div': div1, 'script': script1, 'name': "Всего записей в реестре" + ' - ' + str(g1.summ)})
        figures.append({'div': div2, 'script': script2, 'name': "Прекратило деятельность" + ' - ' + str(g2.count)})
        figures.append({'div': div3, 'script': script3, 'name': "Граф взаимосвязей"})
        figures.append({'div': div4, 'script': script4, 'name': "Регистрация ЮЛ"})
        take_filename = 'dublicate.csv'
        take_data = pd.read_csv(take_filename, sep=',').sort_values(by='Quantity', ascending=False)
        d = take_data[['Index', 'Quantity', 'FIO']].drop_duplicates(subset='Index', keep='first')[0:10]
        dupl_list = d.to_dict(orient='records')
        #print(dupl_list)
        # c_uk = Документ.objects.filter(СвЮЛ__СвОбрЮЛ__СпОбрЮЛ__КодСпОбрЮЛ='03').order_by('-СвЮЛ__ДатаОГРН').count()
        # print(c_uk)
        # uk = Документ.objects.filter(СвЮЛ__СвОбрЮЛ__СпОбрЮЛ__КодСпОбрЮЛ='03').order_by('-СвЮЛ__ДатаОГРН')[0:10]
        # s = ДокументSerializer(uk, many=True)
        #print(s.data)
        # uk_list = json.loads(JSONRenderer().render(s.data).decode('utf8'))
        # print(uk_list)

        context.update(figures=figures, dupl=dupl_list)

        return context

class rest_searchView(TemplateView):

    errors = {"not_found": "Отсутсвуют сведения для заданных параметров поиска",
              "bad_params": "Неверно заданы параметры поиска",
              "internal_err": "Внутренняя ошибка сервера",
              }

    def get_context_data(self, **kwargs):
        print('in pget_context rest_search')
        context = super(rest_searchView, self).get_context_data(**kwargs)
        context.update(form=SearchForm())
        return context

    def get(self, request, *args, **kwargs):
        print('in rest search get')
        return super(rest_searchView, self).get(request, **kwargs)

class searchView(TemplateView):

    errors = {"not_found": "Отсутсвуют сведения для заданных параметров поиска",
              "bad_params": "Неверно заданы параметры поиска",
              "internal_err": "Внутренняя ошибка сервера",
              }

    def get_context_data(self, **kwargs):
        print('in pget_context search')
        context = super(searchView, self).get_context_data(**kwargs)
        context.update(form=SearchForm())
        return context

    def get(self, request, *args, **kwargs):
        print('in search get')
        return super(searchView, self).get(request, **kwargs)

    def post(self, request, *args, **kwargs):
        print('in post searchView')
        errors = []
        result = []
        if not request.is_ajax():
            print('not Ajax')
            return HttpResponseBadRequest('Expected an XMLHttpRequest')
        # print(request.body.decode('utf-8'))
        if request.body:
            in_data = json.loads(request.body.decode('utf-8'))
            form = SearchForm(data=in_data)
            if form.is_valid:
                string_param = in_data['search']
                # print(string_param)
                docs = Документ.objects.annotate().filter(
                    СвЮЛ__СвНаимЮЛ__search_vector=SearchQuery(string_param, config='russian'))
                print('Found -', docs.count())
                if docs:
                    for item in docs:
                        #print(item.СвЮЛ.ОГРН, ' - ', item.СвЮЛ.СвНаимЮЛ.НаимЮЛПолн)
                        result.append(item.get_info())

                response_data = {'errors': form.errors, 'find_errors': errors, 'result': result}
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        print('in error')
        errors.append(self.errors["not_found"])
        response_data = {'errors': form.errors, 'find_errors': errors}
        return HttpResponse(json.dumps(response_data), content_type="application/json")


class EGRIPView(TemplateView):

    def post(self, request, *args, **kwargs):
        print('in post IndexView')
        if not request.is_ajax():
            print('not Ajax')
            return HttpResponseBadRequest('Expected an XMLHttpRequest')
        in_data = json.loads(request.body.decode('utf-8'))
        # print(in_data)
        form = InputForm(data=in_data)
        response_data = {'errors': form.errors, 'search_result': in_data['search']}
        return HttpResponse(json.dumps(response_data), content_type="application/json")

        # bound_contact_form = CheckoutForm(data={'subject': in_data.get('subject')})
        # now validate ‘bound_contact_form’ and use it as in normal Django

    def get_context_data(self, **kwargs):
        print('in pget_context')
        print(self.request)
        print(self.template_name)
        context = super(EGRIPView, self).get_context_data(**kwargs)
        context.update(form=InputForm())
        # form = InputForm()
        # context['form'] = form
        # context['csrf_token'] = 'csrf_token'
        # Тут можно обновить контекст
        print('in EGRIPView')
        return context


class profileView(TemplateView):

    def get_context_data(self, **kwargs):
        print('in profile view')
        context = super(profileView, self).get_context_data(**kwargs)
        #context.update(form=InputForm())
        # form = InputForm()
        # context['form'] = form
        # context['csrf_token'] = 'csrf_token'
        # Тут можно обновить контекст
        return context



