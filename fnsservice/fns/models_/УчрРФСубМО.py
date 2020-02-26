from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвНедДанУчрТип import СвНедДанУчрТип, СвНедДанУчрТипCreate
from .ДоляУстКапЕГРЮЛТип import ДоляУстКапЕГРЮЛТип, ДоляУстКапЕГРЮЛТипCreate
from .СвОбремТип import СвОбремТип, СвОбремТипCreate
from .ВидНаимУчр import ВидНаимУчр, ВидНаимУчрCreate
from .СвОргОсущПр import СвОргОсущПр, СвОргОсущПрCreate
from .СвФЛОсущПр import СвФЛОсущПр, СвФЛОсущПрCreate


class УчрРФСубМО(models.Model): #4.43
    ГРНДатаПерв = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ сведений о данном лице', on_delete=models.DO_NOTHING)
    ВидНаимУчр = models.ForeignKey(ВидНаимУчр, null=True, blank=True,
                                  verbose_name='Сведения о виде учредителя (участника) и (при необходимости) наименовании муниципального образования и региона', on_delete=models.DO_NOTHING)
    СвНедДанУчр = models.ManyToManyField(СвНедДанУчрТип,
                                         verbose_name='Сведения о недостоверности данных об учредителе (участнике) ')

    ДоляУстКап = models.ForeignKey(ДоляУстКапЕГРЮЛТип, null=True, blank=True, verbose_name='Сведения о доле учредителя (участника)', on_delete=models.DO_NOTHING)
    СвОргОсущПр = models.ManyToManyField(СвОргОсущПр, verbose_name='Сведения об органе государственной власти, органе местного самоуправления или о юридическом лице, осуществляющем права учредителя (участника)')

    СвФЛОсущПр = models.ManyToManyField(СвФЛОсущПр, verbose_name='Сведения о физическом лице, осуществляющем права учредителя (участника)')
    СвОб = models.ManyToManyField(СвОбремТип, verbose_name='Сведения об обременении доли участника')

    def __str__(self):
        return '%s - %s' % (self.ГРНДатаПерв, self.ВидНаимУчр.__str__(),)


class УчрРФСубМОCreate:

    def __init__(self, item):
        if item is not None:
            self.ГРНДатаПерв = ГРНДатаТипCreate(item.find('ГРНДатаПерв'))
            self.ВидНаимУчр = ВидНаимУчрCreate(item.find('ВидНаимУчр'))
            self.ДоляУстКап = ДоляУстКапЕГРЮЛТипCreate(item.find('ДоляУстКап'))

            self.a = УчрРФСубМО.objects.create(ГРНДатаПерв=self.ГРНДатаПерв.save(),
                                            ВидНаимУчр=self.ВидНаимУчр.save(),
                                            ДоляУстКап=self.ДоляУстКап.save())

            self.СвНедДанУчр = [СвНедДанУчрТипCreate(i) for i in item.findall('СвНедДанУчр')]
            for one_СвНедДанУчр in self.СвНедДанУчр:
                self.a.СвНедДанУчр.add(one_СвНедДанУчр.save())

            self.СвОргОсущПр = [СвОргОсущПрCreate(i) for i in item.findall('СвОргОсущПр')]
            for one_СвОргОсущПр in self.СвОргОсущПр:
                self.a.СвОргОсущПр.add(one_СвОргОсущПр.save())

            self.СвФЛОсущПр = [СвФЛОсущПрCreate(i) for i in item.findall('СвФЛОсущПр')]
            for one_СвФЛОсущПр in self.СвФЛОсущПр:
                self.a.СвФЛОсущПр.add(one_СвФЛОсущПр.save())

            self.СвОб = [СвОбремТипCreate(i) for i in item.findall('СвОбрем')]
            for one_СвОбрем in self.СвОб:
                self.a.СвОб.add(one_СвОбрем.save())

        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a