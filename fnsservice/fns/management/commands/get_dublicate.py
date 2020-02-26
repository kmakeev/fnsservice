from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from fns.models import Документ
from fns.models_.СвФЛЕГРЮЛТип import СвФЛЕГРЮЛТип
from fns.utils import printProgressBar

#СвУчредит.УчрФЛ.СвФЛЕГРЮЛТип
#СвДовУпрФЛ.СвФЛЕГРЮЛТип
#ЛицоУпрНасл.СвФЛЕГРЮЛТип
#СвФЛОсущПр.СвФЛЕГРЮЛТип
#СвКФХПредш.СвФЛЕГРЮЛТип
#СвКФХПреем.СвФЛЕГРЮЛТип
#СвНотУдДогЗалТип.СвФЛЕГРЮЛТип
#СвЗалогДержФЛ.СвФЛЕГРЮЛТип


#СвФЛЕГРЮЛТип.ИННФЛ


class Command(BaseCommand):
    help = "Get all АД"

    def handle(self, *args, **options):
        print('In Get FL')
        list_FL = СвФЛЕГРЮЛТип.objects.filter(ИННФЛ__isnull=False).values('id')
        count = len(list_FL)
        start = []
        end = []
        index = []
        quantity = []
        fio = []
        j = 0
        for i in list_FL:
            fl = СвФЛЕГРЮЛТип.objects.get(id=i['id'])
            printProgressBar(iteration=j, total=count)
            if int(fl.ИННФЛ) not in index:
                a = Документ.objects.filter(СвЮЛ__СвУчредит__УчрФЛ__СвФЛ__ИННФЛ=fl.ИННФЛ, СвЮЛ__СвПрекрЮЛ__isnull=True)
                b = Документ.objects.filter(СвЮЛ__СвУчредит__УчрФЛ__СвДовУпрФЛ__СвФЛ__ИННФЛ=fl.ИННФЛ, СвЮЛ__СвПрекрЮЛ__isnull=True)
                c = Документ.objects.filter(СвЮЛ__СвУчредит__УчрФЛ__ЛицоУпрНасл__СвФЛ__ИННФЛ=fl.ИННФЛ, СвЮЛ__СвПрекрЮЛ__isnull=True)
                d = Документ.objects.filter(СвЮЛ__СвУчредит__УчрРФСМО__СвФЛОсущПр__СвФЛ__ИННФЛ=fl.ИННФЛ, СвЮЛ__СвПрекрЮЛ__isnull=True)
                e = Документ.objects.filter(СвЮЛ__СвКФХПредш__СвФЛ__ИННФЛ=fl.ИННФЛ, СвЮЛ__СвПрекрЮЛ__isnull=True)
                f = Документ.objects.filter(СвЮЛ__СвКФХПреем__СвФЛ__ИННФЛ=fl.ИННФЛ, СвЮЛ__СвПрекрЮЛ__isnull=True)
                uls = a.union(b, c, d, e, f)
                if len(uls) > 1:
                    # print(fl.Фамилия, ' in - ', len(d), ' doc')
                    for item in uls[1:]:
                        start.append(int(uls[0].СвЮЛ.ОГРН))
                        end.append(int(item.СвЮЛ.ОГРН))
                        index.append(int(fl.ИННФЛ))
                        quantity.append(len(uls))
                        fio.append(str('' if fl.Фамилия is None else fl.Фамилия) + ' ' + str('' if fl.Имя is None else fl.Имя) + ' ' + str('' if fl.Отчество is None else fl.Отчество))
                j += 1
        data = {'Start': start, 'End': end, 'Index': index, 'Quantity': quantity, 'FIO': fio}
        data_frame = pd.DataFrame(data, columns=['Start', 'End', 'Index', 'Quantity', 'FIO']).sort_values(by='Quantity', ascending=False)
        print(data_frame.info())
        data_frame.to_csv('dublicate.csv')

