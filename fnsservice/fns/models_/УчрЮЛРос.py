from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвЮЛЕГРЮЛТип import СвЮЛЕГРЮЛТип, СвЮЛЕГРЮЛТипCreate
from .СвРегСтарые import СвРегСтарые, СвРегСтарыеCreate
from .СвНедДанУчрТип import СвНедДанУчрТип, СвНедДанУчрТипCreate
from .ДоляУстКапЕГРЮЛТип import ДоляУстКапЕГРЮЛТип, ДоляУстКапЕГРЮЛТипCreate
from .СвОбремТип import СвОбремТип, СвОбремТипCreate


class УчрЮЛРос(models.Model): #4.36
    ГРНДатаПерв = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ сведений о данном лице', on_delete=models.DO_NOTHING)
    НаимИННЮЛ = models.ForeignKey(СвЮЛЕГРЮЛТип, null=True, blank=True,
                                 verbose_name='Сведения о наименовании и (при наличии) ОГРН и ИНН ЮЛ', on_delete=models.DO_NOTHING)
    СвРегСтарые = models.ForeignKey(СвРегСтарые, null=True, blank=True,
                                 verbose_name='Сведения о регистрации учредителя (участника) до 01.07.2002 г', on_delete=models.DO_NOTHING)
    СвНУчр = models.ManyToManyField(СвНедДанУчрТип,
                                      verbose_name='Сведения о недостоверности данных об учредителе (участнике) ')
    ДоляУстКап = models.ForeignKey(ДоляУстКапЕГРЮЛТип, null=True, blank=True, verbose_name='Сведения о доле учредителя (участника)', on_delete=models.DO_NOTHING)
    СвОбрем = models.ManyToManyField(СвОбремТип, verbose_name='Сведения об обременении доли участника')



    def __str__(self):
        return '%s - %s' % (self.ДатаПрекрЮЛ, self.СпПрекрЮЛ.__str__,)


class УчрЮЛРосCreate:

    def __init__(self, item):
        if item is not None:
            self.ГРНДатаПерв = ГРНДатаТипCreate(item.find('ГРНДатаПерв'))
            self.НаимИННЮЛ = СвЮЛЕГРЮЛТипCreate(item.find('НаимИННЮЛ'))
            self.СвРегСтарые = СвРегСтарыеCreate(item.find('СвРегСтарые'))
            self.ДоляУстКап = ДоляУстКапЕГРЮЛТипCreate(item.find('ДоляУстКап'))

            self.a = УчрЮЛРос.objects.create(ГРНДатаПерв=self.ГРНДатаПерв.save(),
                                             НаимИННЮЛ=self.НаимИННЮЛ.save(), СвРегСтарые=self.СвРегСтарые.save(),
                                             ДоляУстКап=self.ДоляУстКап.save())
            self.СвНУчр = [СвНедДанУчрТипCreate(i) for i in item.findall('СвНедДанУчр')]
            for one_СвНедДанУчр in self.СвНУчр:
                self.a.СвНУчр.add(one_СвНедДанУчр.save())

            self.СвОбрем = [СвОбремТипCreate(i) for i in item.findall('СвОбрем')]
            for one_СвОбрем in self.СвОбрем:
                self.a.СвОбрем.add(one_СвОбрем.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
