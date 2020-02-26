from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвНедДанУчрТип import СвНедДанУчрТип, СвНедДанУчрТипCreate
from .ДоляУстКапЕГРЮЛТип import ДоляУстКапЕГРЮЛТип, ДоляУстКапЕГРЮЛТипCreate
from .СвНаимПИФ import СвНаимПИФ, СвНаимПИФCreate
from .СвУпрКомпПИФ import СвУпрКомпПИФ, СвУпрКомпПИФCreate
from .СвОбремТип import СвОбремТип, СвОбремТипCreate


class УчрПИФ(models.Model): #4.47
    ГРНДатаПерв = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ сведений о данном лице', on_delete=models.DO_NOTHING)
    СвНаимПИФ = models.ForeignKey(СвНаимПИФ, null=True, blank=True,
                                  verbose_name='Сведения о названии (индивидуальном обозначении) паевого инвестиционного фонда', on_delete=models.DO_NOTHING)
    СвНедДанУчр = models.ManyToManyField(СвНедДанУчрТип,
                                         verbose_name='Сведения о недостоверности данных об учредителе (участнике) ')
    СвУпрКомпПИФ = models.ForeignKey(СвУпрКомпПИФ, null=True, blank=True,
                                  verbose_name='Сведения об управляющей компании паевого инвестиционного фонда', on_delete=models.DO_NOTHING)
    ДоляУстКап = models.ForeignKey(ДоляУстКапЕГРЮЛТип, null=True, blank=True, verbose_name='Сведения о доле учредителя (участника)', on_delete=models.DO_NOTHING)
    СвОбрем = models.ManyToManyField(СвОбремТип, verbose_name='Сведения об обременении доли участника')

    def __str__(self):
        return '%s - %s' % (self.ГРНДатаПерв, self.СвНаимПИФ.__str__(),)


class УчрПИФCreate:

    def __init__(self, item):
        if item is not None:
            self.ГРНДатаПерв = ГРНДатаТипCreate(item.find('ГРНДатаПерв'))
            self.СвНаимПИФ = СвНаимПИФCreate(item.find('СвНаимПИФ'))
            self.СвУпрКомпПИФ = СвУпрКомпПИФCreate(item.find('СвУпрКомпПИФ'))
            self.ДоляУстКап = ДоляУстКапЕГРЮЛТипCreate(item.find('ДоляУстКап'))

            self.a = УчрПИФ.objects.create(ГРНДатаПерв=self.ГРНДатаПерв.save(),
                                           СвНаимПИФ=self.СвНаимПИФ.save(),
                                           СвУпрКомпПИФ=self.СвУпрКомпПИФ.save(),
                                           ДоляУстКап=self.ДоляУстКап.save())

            self.СвНедДанУчр = [СвНедДанУчрТипCreate(i) for i in item.findall('СвНедДанУчр')]
            for one_СвНедДанУчр in self.СвНедДанУчр:
                self.a.СвНедДанУчр.add(one_СвНедДанУчр.save())

            self.СвОбрем = [СвОбремТипCreate(i) for i in item.findall('СвОбрем')]
            for one_СвОбрем in self.СвОбрем:
                self.a.СвОбрем.add(one_СвОбрем.save())

        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
