from django.db import models
from datetime import datetime
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate


class АдрИнЕГРЮЛТип(models.Model):  # 4.81
    ОКСМ = models.CharField(max_length=3, null=True, blank=True,
                                  verbose_name='Код страны')
    НаимСтран = models.CharField(max_length=250, null=True, blank=True,
                                 verbose_name='Наименование страны')
    АдрИн = models.CharField(max_length=510, null=True, blank=True,
                                 verbose_name='Адрес')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='АдрИнЕГРЮЛТип_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s, %s' % (self.НаимСтран, self.АдрИн,)


class АдрИнЕГРЮЛТипCreate:

    def __init__(self, item):
        if item is not None:
            self.ОКСМ = item.get('ОКСМ')
            self.НаимСтран = item.get('НаимСтран')
            self.АдрИн = item.get('АдрИн')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = АдрИнЕГРЮЛТип.objects.create(ОКСМ=self.ОКСМ, НаимСтран=self.НаимСтран, АдрИн=self.АдрИн,
                                                   ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
