from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from fns.models import Документ
from datetime import datetime
from fns.utils import printProgressBar



class Command(BaseCommand):
    help = "Get count by registered UL"

    def handle(self, *args, **options):

        #count_term = Документ.objects.filter(СвЮЛ__СвПрекрЮЛ__isnull=False).count()
        print('In Get registered count')
        print('Save')
        now = datetime.now()
        register_years = []
        counts = []
        counts_together = []
        j = 0
        for year in range(1993, int(now.year), 1):
            j += 1
            printProgressBar(iteration=j, total=int(now.year) - 1993)
            if year < 2002:
                count = Документ.objects.filter(СвЮЛ__СвОбрЮЛ__ДатаРег__year=str(year)).count()
                count_together = 0
            else:
                count = Документ.objects.filter(СвЮЛ__СвОбрЮЛ__ДатаОГРН__year=str(year),
                                                СвЮЛ__СвОбрЮЛ__ДатаРег__isnull=True).count()
                count_together = Документ.objects.filter(СвЮЛ__СвОбрЮЛ__ДатаОГРН__year=str(year)).count()

            # print(year, ' - ', count)
            register_years.append(year)
            counts.append(count)
            counts_together.append(count_together)

        data = {'Register_years': register_years, 'Counts': counts, 'Counts_together': counts_together}
        data_frame = pd.DataFrame(data, columns=['Register_years', 'Counts', 'Counts_together'])
        print(data_frame.info())
        data_frame.to_csv('registered.csv')

