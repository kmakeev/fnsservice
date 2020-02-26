from django.db import models
from datetime import datetime

class СвНПАУтвТУ(models.Model): # 4.26
    НаимГОУтвТУ = models.CharField(max_length=510, null=True, verbose_name='Наименование государственного органа, утвердившего типовой устав')
    ВидНПА = models.CharField(max_length=100, null=True,
                                   verbose_name='Вид нормативного правового акта об утверждении типового устава')
    НаимНПА = models.CharField(max_length=1000, null=True,
                                   verbose_name='Наименование нормативного правового акта об утверждении типового устава')
    НомерНПА = models.CharField(max_length=100, null=True,
                               verbose_name='Номер нормативного правового акта об утверждении типового устава')
    ДатаНПА = models.DateField(auto_now=False, null=True, auto_now_add=False,
                               verbose_name='Дата нормативного правового акта об утверждении типового устава')
    НомерПрил = models.CharField(max_length=100, null=True,
                               verbose_name='Номер приложения')

    def __str__(self):
        return '%s - %s ' % (self.ДатаНПА, self.НомерНПА,)


class СвНПАУтвТУCreate:

    def __init__(self, item):
        if item is not None:
            self.НаимГОУтвТУ = item.get('НаимГОУтвТУ')
            self.ВидНПА = item.get('ВидНПА')
            self.НаимНПА = item.get('НаимНПА')
            self.НомерНПА = item.get('НомерНПА')
            self.ДатаНПА = item.get('ДатаНПА')
            self.НомерПрил = item.get('НомерПрил')
            self.a = СвНПАУтвТУ.objects.create(НаимГОУтвТУ=self.НаимГОУтвТУ, ВидНПА=self.ВидНПА, НомерНПА=self.НомерНПА,
                                               ДатаНПА=datetime.strptime(self.ДатаНПА, '%Y-%m-%d'))
        self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
