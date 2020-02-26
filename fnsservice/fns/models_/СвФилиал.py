from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвНаимПодраздТип import СвНаимПодраздТип, СвНаимПодраздТипCreate
from .АдрРФЕГРЮЛТип import АдрРФЕГРЮЛТип, АдрРФЕГРЮЛТипCreate
from .АдрИнЕГРЮЛТип import АдрИнЕГРЮЛТип, АдрИнЕГРЮЛТипCreate
from .СвУчетНОПодраздТип import СвУчетНОПодраздТип, СвУчетНОПодраздТипCreate


class СвФилиал(models.Model): #4.55
    ГРНДатаПерв = models.ForeignKey(ГРНДатаТип, null=True, blank=True,  verbose_name='ГРН и дата внесения в ЕГРЮЛ сведений о данном филиале', on_delete=models.DO_NOTHING)
    СвНаим = models.ForeignKey(СвНаимПодраздТип, null=True, blank=True, verbose_name='Наименование и (при наличии) ОГРН и ИНН держателе реестра акционеров акционерного общества', on_delete=models.DO_NOTHING)
    АдрМНРФ = models.ForeignKey(АдрРФЕГРЮЛТип, null=True, blank=True,
                               verbose_name='Адрес (место расположения) на территории Российской Федерации', on_delete=models.DO_NOTHING)
    АдрМНИн = models.ForeignKey(АдрИнЕГРЮЛТип, null=True, blank=True,
                                verbose_name='Адрес (место расположения) за пределами территории Российской Федерации', on_delete=models.DO_NOTHING)
    СвУчетНОФилиал = models.ForeignKey(СвУчетНОПодраздТип, null=True, blank=True,
                                verbose_name='Сведения об учете в налоговом органе по месту нахождения филиала', on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'СвФилиал: %s' % (self.СвНаим,)


class СвФилиалCreate:

    def __init__(self, item):
        if item is not None:

            self.ГРНДатаПерв = ГРНДатаТипCreate(item.find('ГРНДатаПерв'))
            self.СвНаим = СвНаимПодраздТипCreate(item.find('СвНаим'))
            self.АдрМНРФ = АдрРФЕГРЮЛТипCreate(item.find('АдрМНРФ'))
            self.АдрМНИн = АдрИнЕГРЮЛТипCreate(item.find('АдрМНИн'))
            self.СвУчетНОФилиал = СвУчетНОПодраздТипCreate(item.find('СвУчетНОФилиал'))

            self.a = СвФилиал.objects.create(ГРНДатаПерв=self.ГРНДатаПерв.save(),
                                             СвНаим=self.СвНаим.save(),
                                             АдрМНРФ=self.АдрМНРФ.save(),
                                             АдрМНИн=self.АдрМНИн.save(),
                                             СвУчетНОФилиал=self.СвУчетНОФилиал.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a