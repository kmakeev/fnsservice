from django.db import models
from datetime import datetime


class РешСудТип(models.Model): # 4.92
    НаимСуда = models.CharField(max_length=1000, null=True, verbose_name='Наименование суда, которым принято решение')
    Номер = models.CharField(max_length=255, null=True, verbose_name='Номер решения')
    Дата = models.DateField(auto_now=False, null=True, auto_now_add=False, verbose_name='Дата решения')

    def __str__(self):
        return 'Решение: %s Решение № %s от %s' % (self.НаимСуда, self.Номер, self.Дата,)


class РешСудТипCreate:
    def __init__(self, solution):
        if solution is not None:
            self.НаимСуда = solution.get('НаимСуда')
            self.Номер = solution.get('Номер')
            self.Дата = solution.get('Дата')
            self.a = РешСудТип.objects.create(НаимСуда=self.НаимСуда, Номер=self.Номер,
                                                Дата=datetime.strptime(self.Дата, '%Y-%m-%d'))
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a

