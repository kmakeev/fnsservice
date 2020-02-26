"""fnsservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from fns.api.apiview import ДокументView, FiltersView, UserView, RequestView
from fns.views.menu import get_menu
from fns.views.pdf import PDFView
from fns.views.portailgroupview import dashboardView, egrulView, searchView, rest_searchView, profileView
from fns.views.index import Index

app_name = 'fns'

portail_patterns = [
    url(r'^dashboard.html$', dashboardView.as_view(template_name='view/dashboard.html'), name='dashboard'),
    url(r'^egrul.html$', egrulView.as_view(template_name='view/egrul.html'), name='egrul'),
    url(r'^requests.html$', profileView.as_view(template_name='view/requests.html'), name='requests'),
    #url(r'^login.html$', loginView.as_view(template_name='view/login.html'), name='login'),
    #url(r'^logout.html$', logoutView.as_view(template_name='view/logout.html'), name='logout'),
    url(r'^search.html$', searchView.as_view(template_name='view/search.html'), name='search'),
    url(r'^rest_search.html$', rest_searchView.as_view(template_name='view/rest_search.html'), name='rest_search'),


]


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name='index'),
    path('pdf/<uuid:id>/', PDFView.as_view(), name='pdf'),
    url(r'^view/', include(portail_patterns)),
    url(r'^menu.html$', get_menu, name='menu'),
    # url(r'^api/uklist/$', UkListView.as_view()),
    url(r'^api/documents/$', ДокументView.as_view()),
    url(r'^api/filters/$', FiltersView.as_view()),
    url(r'^api/user/$', UserView.as_view()),
    url(r'^api/request/$', RequestView.as_view()),
    url(r'^angular-busy.html$', TemplateView.as_view(template_name='angular-busy.html'), name='angular-busy'),
]
