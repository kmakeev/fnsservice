from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from fns.models import Документ
from fns.models_.Св_Статус import Св_Статус
from fns.models import States


class Command(BaseCommand):
    help = "Get count by states UL from base"

    def handle(self, *args, **options):
        print('In Get States')
        states = []
        state_names = []
        counts = []
        for code in range(1000):
            if code < 9:
                str_code = '0' + str(code)
            else:
                str_code = str(code)
            count = Документ.objects.filter(СвЮЛ__СвСтатус__Св_Статус__КодСтатусЮЛ=str_code).count()
            if count > 0:
                state_name = Св_Статус.objects.filter(КодСтатусЮЛ=str_code)[0].НаимСтатусЮЛ           # Нужно определять правильное имя
                # print(str_code, " - ", state_name, " - ", count)
                states.append(str_code)
                state_names.append(state_name + " - " + str(count))
                counts.append(count)
                try:
                    States.objects.get(КодСтатусЮЛ=str_code)
                    print(code, ' exist in database')
                except:
                    m = States.objects.create(КодСтатусЮЛ=str_code, НаимСтатусЮЛ=state_name)
                    m.save()
        count_determ = Документ.objects.filter(СвЮЛ__СвПрекрЮЛ__isnull=False).count()
        print("Деятельность ЮЛ прекращена", " - ", count_determ)
        states.append("201")
        state_names.append("Деятельность ЮЛ прекращена" + " - " + str(count_determ))
        counts.append(count_determ)
        count_active = Документ.objects.filter(СвЮЛ__СвПрекрЮЛ__isnull=True, СвЮЛ__СвСтатус__Св_Статус__isnull=True).count()
        print("Действующее ЮЛ", " - ", count_active)
        states.append("0")
        state_names.append("Действующее ЮЛ" + " - " + str(count_active))
        counts.append(count_active)
        data = {'States': states, 'State_names': state_names, 'Counts': counts}
        data_frame = pd.DataFrame(data, columns=['States', 'State_names', 'Counts'])
        print(data_frame)
        data_frame.to_csv('states.csv')
