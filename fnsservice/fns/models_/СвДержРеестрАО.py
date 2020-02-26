from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвЮЛЕГРЮЛТип import СвЮЛЕГРЮЛТип, СвЮЛЕГРЮЛТипCreate


class СвДержРеестрАО(models.Model): #4.50
    ГРНДатаПерв = models.ForeignKey(ГРНДатаТип, null=True, blank=True,  verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ДержРеестрАО = models.ForeignKey(СвЮЛЕГРЮЛТип, null=True, blank=True, verbose_name='Наименование и (при наличии) ОГРН и ИНН держателе реестра акционеров акционерного общества', on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'СвДержРеестрАО: %s' % (self.ДержРеестрАО,)


class СвДержРеестрАОCreate:

    def __init__(self, item):
        if item is not None:

            self.ГРНДатаПерв = ГРНДатаТипCreate(item.find('ГРНДатаПерв'))
            self.ДержРеестрАО = СвЮЛЕГРЮЛТипCreate(item.find('ДержРеестрАО'))

            self.a = СвДержРеестрАО.objects.create(ГРНДатаПерв=self.ГРНДатаПерв.save(), ДержРеестрАО=self.ДержРеестрАО.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
