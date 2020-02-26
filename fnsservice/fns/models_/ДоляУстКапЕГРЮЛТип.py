from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .РазмерДоли import РазмерДоли, РазмерДолиCreate


class ДоляУстКапЕГРЮЛТип(models.Model): #4.85
    НоминСтоим = models.FloatField(null=True, blank=True, verbose_name='Номинальная стоимость доли в рублях')
    РазмерДоли = models.ForeignKey(РазмерДоли, null=True, blank=True,
                                  verbose_name='Размер доли (в процентах или в виде дроби - десятичной или простой) ', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='ДоляУстКапЕГРЮЛТип_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s р.' % (self.НаимВидКап, self.СумКап,)


class ДоляУстКапЕГРЮЛТипCreate:

    def __init__(self, item):
        if item is not None:
            self.НоминСтоим = item.get('НоминСтоим')
            self.РазмерДоли = РазмерДолиCreate(item.find('РазмерДоли'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = ДоляУстКапЕГРЮЛТип.objects.create(НоминСтоим=float(self.НоминСтоим),
                                                       РазмерДоли=self.РазмерДоли.save(),
                                                       ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
