from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from fns.models import Документ

from fns.utils import printProgressBar


class Command(BaseCommand):
    help = "Get count by terminated UL"

    def handle(self, *args, **options):

        list_term = Документ.objects.filter(СвЮЛ__СвПрекрЮЛ__isnull=False).values('id')
        count_term = len(list_term)
        print('In Get Terminated, find - ', count_term)
        print('Save')
        # all = Документ.objects.filter(СвЮЛ__СвПрекрЮЛ__isnull=False)
        start_dates = []
        end_dates = []
        capitals = []
        addrs = []
        names = []
        ogrns = []
        j = 0
        for i in list_term:
            item = Документ.objects.get(id=i['id'])
            printProgressBar(iteration=j, total=count_term)
            start_date = item.СвЮЛ.ДатаОГРН
            end_date = item.СвЮЛ.СвПрекрЮЛ.ДатаПрекрЮЛ
            ogrn = item.СвЮЛ.ОГРН
            name = item.СвЮЛ.СвНаимЮЛ.НаимЮЛПолн
            if item.СвЮЛ.СвУстКап is not None:
                capital = item.СвЮЛ.СвУстКап.СумКап
            else:
                capital = None
            addr = item.СвЮЛ.СвАдресЮЛ.АдресРФ.КодРегион
            start_dates.append(start_date)
            end_dates.append(end_date)
            capitals.append(capital)
            ogrns.append(ogrn)
            names.append(name)
            addrs.append(addr)
            j += 1
            # print(item.СвЮЛ, " - ", start_date, end_date, kapital, addr)


        data = {'Start_date': start_dates, 'End_date': end_dates, 'Capital': capitals, 'Addr': addrs, 'OGRN': ogrns, 'Name': names}
        data_frame = pd.DataFrame(data, columns=['Start_date', 'End_date', 'Capital', 'Addr', 'OGRN', 'Name'])
        print(data_frame.info())
        data_frame.to_csv('terminated.csv')