from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from fns.models_.СвОКВЭДТип import СвОКВЭДТип
from fns.utils import printProgressBar
from fns.models import OKVED


class Command(BaseCommand):
    help = "Get OKVED"

    def handle(self, *args, **options):
        print('In Get OKVED')
        count = СвОКВЭДТип.objects.all().count()
        print('In base fount -', count, ' records')
        codes = []
        names = []
        ver = []
        processed = []
        j = 0
        for j in range(count):
            ok = СвОКВЭДТип.objects.all()[j]
            printProgressBar(iteration=j, total=count)
            if ok.ПрВерсОКВЭД is not None:
                str_code = ok.ПрВерсОКВЭД + ' ' + ok.КодОКВЭД
            else:
                ПрВерсОКВЭД = '2001'
                str_code = ПрВерсОКВЭД + ' ' + ok.КодОКВЭД
            if str(str_code) not in processed:
                codes.append(ok.КодОКВЭД)
                names.append(ok.НаимОКВЭД)
                ver.append(ok.ПрВерсОКВЭД)
                processed.append(str_code)
                m = OKVED.objects.create(КодОКВЭД=ok.КодОКВЭД, НаимОКВЭД=ok.НаимОКВЭД, ПрВерсОКВЭД=ok.ПрВерсОКВЭД)
                m.save()
        data = {'Codes': codes, 'Names': names, 'Ver': ver}
        data_frame = pd.DataFrame(data, columns=['Codes', 'Names', 'ver'])
        print(data_frame.info())
        data_frame.to_csv('okved.csv')