from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from fns.models import СвЮЛ, Документ, FilterBlock
from fns.models import ДокументSerializer, FilterBlockSerializer
from celeryApp.models import Request, RequestSerializer
import rest_framework_filters as filters
import django_filters
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery

from django.contrib.auth import authenticate, login, logout


from celeryApp.tasks import check_update
# from django_filters.rest_framework import DjangoFilterBackend


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):

        count_ = self.page.paginator.count
        final_ = self.page.paginator.num_pages
        current_page = self.page.number
        # print(_get_displayed_page_numbers(current_page, final_))
        if final_ <= 10:
            start_page = 1
            end_page = final_
        else:
            if current_page <= 6:
                start_page = 1
                end_page = 10
            elif (current_page + 4) >= final_:
                start_page = final_ - 9
                end_page = final_
            else:
                start_page = current_page - 5
                end_page = current_page + 4
        list_pages = [i for i in range(start_page, end_page + 1, 1)]

        return Response({
            'count': count_,
            'num_pages': final_,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'currentPage': current_page,
            'pages': list_pages,
            'results': data
        })


class FilterResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):

        count_ = self.page.paginator.count
        final_ = self.page.paginator.num_pages
        current_page = self.page.number
        # print(_get_displayed_page_numbers(current_page, final_))
        if final_ <= 10:
            start_page = 1
            end_page = final_
        else:
            if current_page <= 6:
                start_page = 1
                end_page = 10
            elif (current_page + 4) >= final_:
                start_page = final_ - 9
                end_page = final_
            else:
                start_page = current_page - 5
                end_page = current_page + 4
        list_pages = [i for i in range(start_page, end_page + 1, 1)]

        return Response({
            'count': count_,
            'num_pages': final_,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'currentPage': current_page,
            'pages': list_pages,
            'results': data
        })


class FiltersView(APIView):

    serializer_class = FilterBlockSerializer

    def get(self, request):
        print('In get Filter2View')
        queryset = FilterBlock.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response({'data': serializer.data})


class ДокументFilter(filters.FilterSet):

    disqualification = filters.BooleanFilter(name='СвЮЛ__СведДолжнФЛ__СвДискв', lookup_expr='isnull')
    codeEduMethod = filters.CharFilter(name='СвЮЛ__СвОбрЮЛ__СпОбрЮЛ__КодСпОбрЮЛ')
    region = filters.CharFilter(name='СвЮЛ__СвАдресЮЛ__АдресРФ__КодРегион')
    search = filters.CharFilter(method='complex_search_filter')
    fio = filters.CharFilter(method='complex_fio_filter')
    reg_start_date = filters.DateFilter(name='СвЮЛ__ДатаОГРН', lookup_expr='gte')
    reg_end_date = filters.DateFilter(name='СвЮЛ__ДатаОГРН', lookup_expr='lte')
    state = filters.CharFilter(name='СвЮЛ__СвСтатус__Св_Статус__КодСтатусЮЛ')
    isactive = filters.BooleanFilter(method='is_active_filter')

    isAddrFalsity = filters.BooleanFilter(method='check_addr_falsity')
    isAddrChange = filters.BooleanFilter(method='check_addr_сhange')
    isemail = filters.BooleanFilter(method='check_email_filter')
    email = filters.CharFilter(name='СвЮЛ__СвАдрЭлПочты__E_mail', lookup_expr='icontains')
    index = filters.CharFilter(name='СвЮЛ__СвАдресЮЛ__АдресРФ__Индекс', lookup_expr='icontains')
    codeKLADR = filters.CharFilter(name='СвЮЛ__СвАдресЮЛ__АдресРФ__КодАдрКладр', lookup_expr='icontains')
    area = filters.CharFilter(name='СвЮЛ__СвАдресЮЛ__АдресРФ__Район__НаимРайон', lookup_expr='icontains')
    city = filters.CharFilter(name='СвЮЛ__СвАдресЮЛ__АдресРФ__Город__НаимГород', lookup_expr='icontains')
    locality = filters.CharFilter(name='СвЮЛ__СвАдресЮЛ__АдресРФ__НаселПункт__НаимНаселПункт', lookup_expr='icontains')
    street = filters.CharFilter(name='СвЮЛ__СвАдресЮЛ__АдресРФ__Улица__НаимУлица', lookup_expr='icontains')
    regNum = filters.CharFilter(name='СвЮЛ__СвОбрЮЛ__РегНом', lookup_expr='icontains')
    startregDate = filters.DateFilter(name='СвЮЛ__СвОбрЮЛ__ДатаРег', lookup_expr='gte')
    endregDate = filters.DateFilter(name='СвЮЛ__СвОбрЮЛ__ДатаРег', lookup_expr='lte')
    isChartCapital = filters.BooleanFilter(method='check_isChartCapital')
    nameCapital = filters.CharFilter(name='СвЮЛ__СвУстКап__НаимВидКап', lookup_expr='icontains')
    summCap = filters.CharFilter(name='СвЮЛ__СвУстКап__СумКап', lookup_expr='lte')
    isSvUprOrg = filters.BooleanFilter(method='check_isSvUprOrg')
    nameUprOrg = filters.CharFilter(method='complex_UprOrg_filter')
    isSvWithoutAtt = filters.BooleanFilter(method='check_isSvWithoutAtt')
    fioWA = filters.CharFilter(method='complex_fioWA_filter')
    isFounder = filters.BooleanFilter(method='check_isFounder')
    isFRus = filters.BooleanFilter(method='check_isFRus')
    isFFl = filters.BooleanFilter(method='check_isFFl')
    isFGOS = filters.BooleanFilter(method='check_isFGOS')
    isFIn = filters.BooleanFilter(method='check_isFIn')

    okved = filters.CharFilter(method='okved_filter')
    okvedtxt = filters.CharFilter(method='okved_filter')

    numberL = filters.CharFilter(name='СвЮЛ__СвЛицензия__НомЛиц', lookup_expr='icontains', distinct=True)
    startLicense = filters.DateFilter(name='СвЮЛ__СвЛицензия__ДатаНачЛиц', lookup_expr='gte', distinct=True)
    endLicense = filters.DateFilter(name='СвЮЛ__СвЛицензия__ДатаОкончЛиц', lookup_expr='lte', distinct=True)

    nameL = filters.CharFilter(method='license_filter')

    grn = filters.CharFilter(name='СвЮЛ__СвЗапЕГРЮЛ__ГРН', lookup_expr='icontains', distinct=True)
    startRecord = filters.DateFilter(name='СвЮЛ__СвЗапЕГРЮЛ__ДатаЗап', lookup_expr='gte', distinct=True)
    endRecord = filters.DateFilter(name='СвЮЛ__СвЗапЕГРЮЛ__ДатаЗап', lookup_expr='lte', distinct=True)
    declarer = filters.CharFilter(method='complex_declarer_filter')
    documents = filters.CharFilter(name='СвЮЛ__СвЗапЕГРЮЛ__СведПредДок__НаимДок', lookup_expr='icontains', distinct=True)


    class Meta:
        model = Документ
        fields = {'id', 'ИдДок', 'СвЮЛ', }


    def complex_search_filter(self, qs, name, value):
        #print(qs.count())
        if value.find(' ') == -1:
            qs_ = qs.filter(Q(СвЮЛ__ОГРН__icontains=value) | Q(СвЮЛ__ИНН__icontains=value) | Q(
                СвЮЛ__СвНаимЮЛ__НаимЮЛСокр__icontains=value) | Q(СвЮЛ__СвНаимЮЛ__НаимЮЛПолн__icontains=value)).distinct()
        else:
            qs_ = qs.filter(СвЮЛ__СвНаимЮЛ__search_vector=SearchQuery(value, config='russian'))

        # qs2 = qs.filter(СвЮЛ__ИНН__icontains=value)
        #print(qs_.count())

        return qs_

    def complex_UprOrg_filter(self, qs, name, value):
        # print(qs.count())
        if value.find(' ') == -1:
            qs_ = qs.filter(Q(СвЮЛ__СвУпрОрг__НаимИННЮЛ__ОГРН__icontains=value) | Q(СвЮЛ__СвУпрОрг__НаимИННЮЛ__ИНН__icontains=value) | Q(
                СвЮЛ__СвУпрОрг__НаимИННЮЛ__НаимЮЛПолн__icontains=value)).distinct()
        else:
            qs_ = qs.filter(СвЮЛ__СвУпрОрг__search_vector=SearchQuery(value, config='russian'))

        # qs2 = qs.filter(СвЮЛ__ИНН__icontains=value)
        # print(qs_.count())

        return qs_


    def complex_fio_filter(self, qs, name, value):
        #print(qs.count(), name, value)
        qs1 = qs.filter(Q(СвЮЛ__СвУчредит__УчрФЛ__СвФЛ__search_vector=SearchQuery(value, config='russian')) |
                        Q(СвЮЛ__СвУчредит__УчрФЛ__СвФЛ__ИННФЛ__icontains=value) |
                        Q(СвЮЛ__СвУчредит__УчрФЛ__СвДовУпрФЛ__СвФЛ__search_vector=SearchQuery(value, config='russian')) |
                        Q(СвЮЛ__СвУчредит__УчрФЛ__СвДовУпрФЛ__СвФЛ__ИННФЛ__icontains=value)).distinct()
        #qs2 = qs.filter(

        #qs_ = qs1.union(qs2).all()
        #print(qs1.count())
        #print(qs2.count())
        #print(qs_.count())




                                   #Q(СвЮЛ__СвУчредит__УчрФЛ__СвДовУпрФЛ__СвФЛ__search_vector=SearchQuery(value, config='russian')) |
                                   #Q(СвЮЛ__СвУчредит__УчрФЛ__ЛицоУпрНасл__СвФЛ__search_vector=SearchQuery(value, config='russian')) |
                                   #Q(СвЮЛ__СвУчредит__УчрРФСМО__СвФЛОсущПр__СвФЛ__search_vector=SearchQuery(value, config='russian')) |
                                   #Q(СвЮЛ__СвКФХПредш__СвФЛ__search_vector=SearchQuery(value, config='russian')) |
                                   #Q(СвЮЛ__СвКФХПреем__СвФЛ__search_vector=SearchQuery(value, config='russian')))

        #print(len(qs_))

        return qs1

    def complex_fioWA_filter(self, qs, name, value):
        # print(qs.count(), name, value)
        #qs1 = qs.filter(СвЮЛ__СведДолжнФЛ__СвФЛ__ИННФЛ__icontains=value)

        qs1 = qs.filter(Q(СвЮЛ__СведДолжнФЛ__СвФЛ__search_vector=SearchQuery(value, config='russian')) |
                        Q(СвЮЛ__СведДолжнФЛ__СвФЛ__ИННФЛ__icontains=value)).distinct()

        return qs1

    def complex_declarer_filter(self, qs, name, value):
        # print(qs.count(), name, value)
        # qs1 = qs.filter(СвЮЛ__СведДолжнФЛ__СвФЛ__ИННФЛ__icontains=value)

        qs1 = qs.filter(Q(СвЮЛ__СвЗапЕГРЮЛ__СвЗФЛ__СвФЛ__СвФИОИНН__search_vector=SearchQuery(value, config='russian'))|
                        Q(СвЮЛ__СвЗапЕГРЮЛ__СвЗФЛ__СвФЛ__СвФИОИНН__ИННФЛ__icontains=value)).distinct()


        return qs1

    def okved_filter(self, qs, name, value):
        # qs1 = qs.filter(СвЮЛ__СведДолжнФЛ__СвФЛ__ИННФЛ__icontains=value)

        qs1 = qs.filter(Q(СвЮЛ__СвОКВЭД__СвОКВЭДОсн__КодОКВЭД__exact=value) |
                        Q(СвЮЛ__СвОКВЭД__СвОКВЭДДоп__КодОКВЭД__exact=value) |
                        Q(СвЮЛ__СвОКВЭД__СвОКВЭДОсн__search_vector=SearchQuery(value, config='russian')) |
                        Q(СвЮЛ__СвОКВЭД__СвОКВЭДДоп__search_vector=SearchQuery(value, config='russian'))).distinct()

        #Q(СвЮЛ__СвОКВЭД__СвОКВЭДОсн__КодОКВЭД__search_vector=SearchQuery(value, config='russian')) |

        return qs1

    def license_filter(self, qs, name, value):
        qs1 = qs.filter(СвЮЛ__СвЛицензия__search_vector=SearchQuery(value, config='russian')).distinct()

        return qs1

    def check_addr_сhange(self, qs, name, value):
        if value is False:
            qs_ = qs
        else:
            qs_ = qs.filter(СвЮЛ__СвАдресЮЛ__СвРешИзмМН__isnull=False).distinct()

        return qs_

    def check_addr_falsity(self, qs, name, value):
        if value is False:
            qs_ = qs
        else:
            qs_ = qs.filter(СвЮЛ__СвАдресЮЛ__СвНедАдресЮЛ__isnull=False).distinct()

        return qs_

    def check_email_filter(self, qs, name, value):
        if value is False:
            qs_ = qs
        else:
            qs_ = qs.filter(СвЮЛ__СвАдрЭлПочты__isnull=False).distinct()

        return qs_

    def check_isChartCapital(self, qs, name, value):
        if value is False:
            qs_ = qs
        else:
            qs_ = qs.filter(СвЮЛ__СвУстКап__isnull=False).distinct()

        return qs_

    def check_isSvUprOrg(self, qs, name, value):
        if value is False:
            qs_ = qs
        else:
            qs_ = qs.filter(СвЮЛ__СвУпрОрг__isnull=False).distinct()

        return qs_

    def check_isSvWithoutAtt(self, qs, name, value):
        if value is False:
            qs_ = qs
        else:
            qs_ = qs.filter(СвЮЛ__СведДолжнФЛ__isnull=False).distinct()

        return qs_

    def check_isFounder(self, qs, name, value):
        if value is False:
            qs_ = qs
        else:
            qs_ = qs.filter(СвЮЛ__СвУчредит__isnull=False).distinct()

        return qs_

    def check_isFRus(self, qs, name, value):
        if value is False:
            qs_ = qs
        else:
            qs_ = qs.filter(СвЮЛ__СвУчредит__УчрЮЛРос__isnull=False).distinct()

        return qs_

    def check_isFFl(self, qs, name, value):
        # print(name, value)
        if value is False:
            qs_ = qs
        else:
            qs_ = qs.filter(СвЮЛ__СвУчредит__УчрФЛ__isnull=False).distinct()

        return qs_

    def check_isFGOS(self, qs, name, value):
        if value is False:
            qs_ = qs
        else:
            qs_ = qs.filter(СвЮЛ__СвУчредит__УчрРФСМО__isnull=False).distinct()

        return qs_

    def check_isFIn(self, qs, name, value):
        if value is False:
            qs_ = qs
        else:
            qs_ = qs.filter(СвЮЛ__СвУчредит__УчрЮЛИн__isnull=False).distinct()

        return qs_

    def is_active_filter(self, qs, name, value):
        if value is False:
            qs_ = qs.filter(СвЮЛ__СвПрекрЮЛ__isnull=False).distinct()
        else:
            qs_ = qs.filter(СвЮЛ__СвПрекрЮЛ__isnull=True).distinct()

        return qs_


class ДокументView(generics.ListAPIView):

    queryset = Документ.objects.all().order_by('id')
    pagination_class = StandardResultsSetPagination
    serializer_class = ДокументSerializer
    filter_backends = (filters.backends.DjangoFilterBackend,)
    # filter_backends = (filters.backends.ComplexFilterBackend,)
    # filter_fields = {'ИдДок', 'id'}

    def get(self, request):
        print('In get FilterView')
        # print(self.queryset.count())
        filter_set = ДокументFilter(request.GET, queryset=self.queryset).qs
        print(filter_set.count(), '/', self.queryset.count())
        page = self.paginate_queryset(filter_set)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

    @property
    def paginator(self):

        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):

        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):

        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


class UserView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):

        if request.user.is_authenticated:
            content = {
                'id': request.user.id,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                # 'auth': request.auth,  # None
            }
            return Response(content)
        else:
            content = {'Unauthorised': 'This API is private'}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, format=None):
        logout(request)
        content = {'Status': 'OK'}
        return Response(content)


class RequestFilter(filters.FilterSet):

    #idreq = filters.BooleanFilter(name='idreq', lookup_expr='isnull')
    code = filters.CharFilter(method='check_code')

    class Meta:
        model = Request
        fields = ('idreq', 'datereq', 'service', 'method', 'code', 'notsignfilename', 'reqfilename',
                  'resfilename', 'params', 'dateres',)

    def check_code(self, qs, name, value):

        """Временно без beat сервиса"""
        check_update.s()()

        if value == 'all':
            #qs_ = qs.filter(method__in=['SendShortFLRequest', 'SendFullULRequest'])
            # qs_ = qs.order_by('-datereq')
            print(qs.count())
            qs_ = qs.order_by('root_id').distinct('root_id')
        elif value =='process':
            qs_ = qs.filter(method__in=['GetFullULResponse', 'GetShortULResponse'], code__in=['52']).order_by('root_id').distinct('root_id')
        elif value == 'resolved':
            qs_ = qs.filter(code__in=['01', '53', '82', '83', '97', '98', '99']).order_by('root_id').distinct(
                'root_id')
        else:
            qs_ = qs
        return qs_


class RequestView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Request.objects.using('req').all().order_by('-id')
    pagination_class = StandardResultsSetPagination
    serializer_class = RequestSerializer

    def get(self, request, format=None):

        print('In ger Request filter, user - ', request.user)
        filter_set = RequestFilter(request.GET, queryset=self.queryset.filter(user=request.user)).qs
        print(filter_set.count(), '/', self.queryset.count())
        page = self.paginate_queryset(filter_set)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

    @property
    def paginator(self):

        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):

        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):

        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)