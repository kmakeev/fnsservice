from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from datetime import datetime


class СвДискв(models.Model): #4.34

    ДатаНачДискв = models.DateField(auto_now=False, null=True, auto_now_add=False, verbose_name='Дата начала дисквалификации')
    ДатаОкончДискв = models.DateField(auto_now=False, null=True, auto_now_add=False,
                                    verbose_name='Дата окончания дисквалификации')
    ДатаРеш = models.DateField(auto_now=False, null=True, auto_now_add=False,
                                    verbose_name='Дата вынесения судебным органом постановления о дисквалификации ')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвДискв_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s ' % (self.ДатаНачДискв, self.ДатаОкончДискв,)


class СвДисквCreate:

    def __init__(self, item):
        if item is not None:
            self.ДатаНачДискв = item.get('ДатаНачДискв')
            self.ДатаОкончДискв = item.get('ДатаОкончДискв')
            self.ДатаРеш = item.get('ДатаРеш')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвДискв.objects.create(ДатаНачДискв=datetime.strptime(self.ДатаНачДискв, '%Y-%m-%d'),
                                            ДатаОкончДискв=datetime.strptime(self.ДатаОкончДискв, '%Y-%m-%d'),
                                            ДатаРеш=datetime.strptime(self.ДатаРеш, '%Y-%m-%d'),
                                            ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a