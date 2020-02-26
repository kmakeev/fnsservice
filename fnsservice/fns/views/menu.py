from django.http import HttpResponse, JsonResponse
from django.views import View
from django.template import loader
import json


def get_menu(request):

    menu = [{"title": "Обзор",
             "href": "#!",
             "href_test": "/"},
            {"title": "ЕГРЮЛ",
             "href": "#!egrul",
             "href_test": "/egrul"},
            {"title": "Поиск",
             "href": "#!search",
             "href_test": "/search"}
            ]

    print('in get menu')

    return HttpResponse(json.dumps(menu), content_type="application/json")


