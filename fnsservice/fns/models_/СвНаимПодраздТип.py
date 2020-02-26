from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate


class СвНаимПодраздТип(models.Model): #4.93
    НаимПолн = models.CharField(max_length=1000, null=True, verbose_name='Наименование')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвНаимПодраздТип_Дата', verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True, verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s' % (self.СНаимПолн,)


class СвНаимПодраздТипCreate:

    def __init__(self, item):
        if item is not None:
            self.НаимПолн = item.get('НаимПолн')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвНаимПодраздТип.objects.create(НаимПолн=self.НаимПолн,
                                              ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a