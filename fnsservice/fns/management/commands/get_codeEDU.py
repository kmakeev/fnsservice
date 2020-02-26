from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from fns.models import Документ, ModeEducation
from fns.models_.СпОбрЮЛ import СпОбрЮЛ


class Command(BaseCommand):
    help = "Get Code of educations UL from base"

    def handle(self, *args, **options):
        print('In Get code')
        codes = []
        codes_names = []
        counts = []
        for code in range(100):
            if code < 9:
                str_code = '0' + str(code)
            else:
                str_code = str(code)
            count = Документ.objects.filter(СвЮЛ__СвОбрЮЛ__СпОбрЮЛ__КодСпОбрЮЛ=str_code).count()
            if count > 0:
                code_name = СпОбрЮЛ.objects.filter(КодСпОбрЮЛ=str_code)[0].НаимСпОбрЮЛ
                print(str_code, " - ", code_name, " - ", count)
                codes.append(str_code)
                codes_names.append(code_name)
                counts.append(count)
                try:
                    ModeEducation.objects.get(КодСпОбрЮЛ=str_code)
                    print(code, ' exist in database')
                except:
                    m = ModeEducation.objects.create(КодСпОбрЮЛ=str_code, НаимСпОбрЮЛ=code_name)
                    m.save()

        data = {'Codes': codes, 'Codes_names': codes_names, 'Counts': counts}
        data_frame = pd.DataFrame(data, columns=['Code', 'Codes_names', 'Counts'])
        print(data_frame)
        data_frame.to_csv('codesEdu.csv')
