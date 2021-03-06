from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from datetime import datetime
from .СвНОТип import СвНОТип, СвНОТипCreate


class СвУчетНОПодраздТип(models.Model): #4.105

    КПП = models.CharField(max_length=9, null=True, verbose_name='КПП юридического лица')
    ДатаПостУч = models.DateField(auto_now=False, null=True, auto_now_add=False, verbose_name='Дата постановки на учет в налоговом органе')
    СвНО = models.ForeignKey(СвНОТип, null=True, blank=True,
                                  verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвУчетНОПодраздТип_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.ДатаПостУч,  self.КПП,)


class СвУчетНОПодраздТипCreate:

    def __init__(self, item):
        if item is not None:
            self.КПП = item.get('КПП')
            self.ДатаПостУч = item.get('ДатаПостУч')
            self.СвНО = СвНОТипCreate(item.find('СвНО'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвУчетНОПодраздТип.objects.create(КПП=self.КПП,
                                             СвНО=self.СвНО.save(),
                                             ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
            if self.ДатаПостУч is not None:
                self.a.ДатаПостУч = datetime.strptime(self.ДатаПостУч, '%Y-%m-%d')
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a