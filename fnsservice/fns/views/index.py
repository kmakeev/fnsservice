from django.http import HttpResponse
from django.views import View
from django.template import loader
from django.utils import timezone
import datetime
from fns.forms.login_form import LoginForm
import json
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt


class Index(View):

    template = loader.get_template('base.html')

    def get(self, request, *args, **kwargs):
        # form = InputForm()
        print('in IndexView')
        form = LoginForm()

        if not request.user.is_authenticated:
            request.session.set_expiry(None)
            if 'key' not in request.session:
                request.session['last_date'] = str(datetime.datetime.now())
                request.session.save()
                request.session['key'] = request.session.session_key
        else:
            pass
        context = {'path': request.path, 'form': form}

        return HttpResponse(self.template.render(context, request))

    def post(self, request, *args, **kwargs):
        print('in post IndexView')
        # if request.user.is_authenticated:
        #    print('User is authenticated')
        #    return HttpResponseRedirect(reverse_lazy('index'))

        if not request.is_ajax():
            print('not Ajax')
            return HttpResponseBadRequest('Expected an XMLHttpRequest')
        # print(request.body.decode('utf-8'))
        if request.body:
            in_data = json.loads(request.body.decode('utf-8'))
            form = LoginForm(data=in_data)
            if form.is_valid():
                user_ = in_data['login']
                password_ = in_data['password']
                user = authenticate(username=user_, password=password_)
                if user is not None:
                    login(request, user)
                    response_data = {'errors': form.errors}
                    return HttpResponse(json.dumps(response_data), content_type="application/json")

        #print('form is invalid', form)
        response_data = {'errors': form.errors}
        return HttpResponse(json.dumps(response_data), content_type="application/json")






