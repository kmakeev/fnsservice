from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвФЛЕГРЮЛТип import СвФЛЕГРЮЛТип, СвФЛЕГРЮЛТипCreate
from .СвРождЕГРЮЛТип import СвРождЕГРЮЛТип, СвРождЕГРЮЛТипCreate
from .СвНедДанУчрТип import СвНедДанУчрТип, СвНедДанУчрТипCreate
from .ДоляУстКапЕГРЮЛТип import ДоляУстКапЕГРЮЛТип, ДоляУстКапЕГРЮЛТипCreate
from .СвОбремТип import СвОбремТип, СвОбремТипCreate
from .УдЛичнЕГРЮЛТип import УдЛичнЕГРЮЛТип, УдЛичнЕГРЮЛТипCreate
from .АдрРФЕГРЮЛТип import АдрРФЕГРЮЛТип, АдрРФЕГРЮЛТипCreate
from .АдрИнЕГРЮЛТип import АдрИнЕГРЮЛТип, АдрИнЕГРЮЛТипCreate
from .СвДовУпрЮЛ import СвДовУпрЮЛ, СвДовУпрЮЛCreate
from .СвДовУпрФЛ import СвДовУпрФЛ,  СвДовУпрФЛCreate
from .ЛицоУпрНасл import ЛицоУпрНасл, ЛицоУпрНаслCreate


class УчрФЛ(models.Model): #4.39
    ГРНДатаПерв = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ сведений о данном лице', on_delete=models.DO_NOTHING)
    СвФЛ = models.ForeignKey(СвФЛЕГРЮЛТип, null=True, blank=True,
                                 verbose_name='Сведения о ФИО и (при наличии) ИНН ФЛ', on_delete=models.DO_NOTHING)
    СвНедДанУчр = models.ManyToManyField(СвНедДанУчрТип,
                                         verbose_name='Сведения о недостоверности данных об учредителе (участнике) ')
    СвРождФЛ = models.ForeignKey(СвРождЕГРЮЛТип, null=True, blank=True,
                                 verbose_name='Сведения о рождении ФЛ', on_delete=models.DO_NOTHING)
    УдЛичнФЛ = models.ForeignKey(УдЛичнЕГРЮЛТип, null=True, blank=True,
                                 verbose_name='Сведения о документе, удостоверяющем личность', on_delete=models.DO_NOTHING)
    АдресМЖРФ = models.ForeignKey(АдрРФЕГРЮЛТип, null=True, blank=True,
                                  verbose_name='Сведения об адресе места жительства в Российской Федерации', on_delete=models.DO_NOTHING)
    АдрМЖИн = models.ForeignKey(АдрИнЕГРЮЛТип, null=True, blank=True,
                                verbose_name='Сведения об адресе места жительства за пределами территории Российской Федерации', on_delete=models.DO_NOTHING)

    ДоляУстКап = models.ForeignKey(ДоляУстКапЕГРЮЛТип, null=True, blank=True, verbose_name='Сведения о доле учредителя (участника)', on_delete=models.DO_NOTHING)
    СвОбрем = models.ManyToManyField(СвОбремТип, verbose_name='Сведения об обременении доли участника')
    СвДовУпрЮЛ = models.ForeignKey(СвДовУпрЮЛ, null=True, blank=True, verbose_name='Сведения о доверительном управляющем - ЮЛ ', on_delete=models.DO_NOTHING)
    СвДовУпрФЛ = models.ForeignKey(СвДовУпрФЛ, null=True, blank=True, verbose_name='Сведения о доверительном управляющем - ФЛ', on_delete=models.DO_NOTHING)
    ЛицоУпрНасл = models.ForeignKey(ЛицоУпрНасл, null=True, blank=True, verbose_name='Сведения о лице, осуществляющем управление долей, переходящей в порядке наследования', on_delete=models.DO_NOTHING)



    def __str__(self):
        return '%s - %s' % (self.ДатаПрекрЮЛ, self.СпПрекрЮЛ.__str__,)


class УчрФЛCreate:

    def __init__(self, item):
        if item is not None:
            self.ГРНДатаПерв = ГРНДатаТипCreate(item.find('ГРНДатаПерв'))
            self.СвФЛ = СвФЛЕГРЮЛТипCreate(item.find('СвФЛ'))
            self.СвРождФЛ = СвРождЕГРЮЛТипCreate(item.find('СвРождФЛ'))
            self.УдЛичнФЛ = УдЛичнЕГРЮЛТипCreate(item.find('УдЛичнФЛ'))
            self.АдресМЖРФ = АдрРФЕГРЮЛТипCreate(item.find('АдресМЖРФ'))
            self.АдрМЖИн = АдрИнЕГРЮЛТипCreate(item.find('АдрМЖИн'))
            self.ДоляУстКап = ДоляУстКапЕГРЮЛТипCreate(item.find('ДоляУстКап'))
            self.СвДовУпрЮЛ = СвДовУпрЮЛCreate(item.find('СвДовУпрЮЛ'))
            self.СвДовУпрФЛ = СвДовУпрФЛCreate(item.find('СвДовУпрФЛ'))
            self.ЛицоУпрНасл = ЛицоУпрНаслCreate(item.find('ЛицоУпрНасл'))

            self.a = УчрФЛ.objects.create(ГРНДатаПерв=self.ГРНДатаПерв.save(),
                                          СвФЛ=self.СвФЛ.save(),
                                          СвРождФЛ=self.СвРождФЛ.save(),
                                          УдЛичнФЛ=self.УдЛичнФЛ.save(),
                                          АдресМЖРФ=self.АдресМЖРФ.save(),
                                          АдрМЖИн=self.АдрМЖИн.save(),
                                          ДоляУстКап=self.ДоляУстКап.save(),
                                          СвДовУпрЮЛ=self.СвДовУпрЮЛ.save(),
                                          СвДовУпрФЛ=self.СвДовУпрФЛ.save(),
                                          ЛицоУпрНасл=self.ЛицоУпрНасл.save())

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
