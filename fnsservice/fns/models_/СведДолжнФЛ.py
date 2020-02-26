from django.db import models
from .СвНомТелТип import СвНомТелТип, СвНомТелТипCreate
from .СвРождЕГРЮЛТип import СвРождЕГРЮЛТип, СвРождЕГРЮЛТипCreate
from .УдЛичнЕГРЮЛТип import УдЛичнЕГРЮЛТип, УдЛичнЕГРЮЛТипCreate
from .АдрРФЕГРЮЛТип import АдрРФЕГРЮЛТип, АдрРФЕГРЮЛТипCreate
from .АдрИнЕГРЮЛТип import АдрИнЕГРЮЛТип, АдрИнЕГРЮЛТипCreate
from .СвДолжн import СвДолжн, СвДолжнCreate
from .СвФЛЕГРЮЛТип import СвФЛЕГРЮЛТип, СвФЛЕГРЮЛТипCreate
from .СвНедДанДолжнФЛ import СвНедДанДолжнФЛ, СвНедДанДолжнФЛCreate
from .СвДискв import СвДискв, СвДисквCreate
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
import datetime


class СведДолжнФЛ(models.Model): # 4.31

    ГРНДатаПерв = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ сведений о данном лице', on_delete=models.DO_NOTHING)
    СвФЛ = models.ForeignKey(СвФЛЕГРЮЛТип, null=True, blank=True, verbose_name='Сведения о ФИО и (при наличии) ИНН ФЛ',
                                on_delete=models.DO_NOTHING)
    СвДолжн = models.ForeignKey(СвДолжн, null=True, blank=True, verbose_name='Сведения о должности ФЛ', on_delete=models.DO_NOTHING)
    СвНомТел = models.ForeignKey(СвНомТелТип, null=True, blank=True, verbose_name='Сведения о контактном телефоне ФЛ', on_delete=models.DO_NOTHING)
    СвН = models.ManyToManyField(СвНедДанДолжнФЛ,
                             verbose_name='Сведения о недостоверности данных о лице, имеющем право без доверенности действовать от имени юридического лица')
    СвРождФЛ = models.ForeignKey(СвРождЕГРЮЛТип, null=True, blank=True, verbose_name='Сведения о рождении ФЛ', on_delete=models.DO_NOTHING)
    УдЛичнФЛ = models.ForeignKey(УдЛичнЕГРЮЛТип, null=True, blank=True,
                                 verbose_name='Сведения о документе, удостоверяющем личность', on_delete=models.DO_NOTHING)
    АдресМЖРФ = models.ForeignKey(АдрРФЕГРЮЛТип, null=True, blank=True,
                                 verbose_name='Сведения об адресе места жительства в Российской Федерации', on_delete=models.DO_NOTHING)
    АдрМЖИн = models.ForeignKey(АдрИнЕГРЮЛТип, null=True, blank=True,
                                  verbose_name='Сведения об адресе места жительства за пределами территории Российской Федерации', on_delete=models.DO_NOTHING)
    СвДискв = models.ForeignKey(СвДискв, null=True, blank=True,
                                verbose_name='Сведения о дисквалификации', on_delete=models.DO_NOTHING)


    def __str__(self):
        return '%s - %s' % (self.ГРНДатаПерв, self.СвДолжн.__str__(),)


class СведДолжнФЛCreate:

    def __init__(self, item):
        if item is not None:
            self.ГРНДатаПерв = ГРНДатаТипCreate(item.find('ГРНДатаПерв'))
            self.СвДолжн = СвДолжнCreate(item.find('СвДолжн'))
            self.СвФЛ = СвФЛЕГРЮЛТипCreate(item.find('СвФЛ'))
            self.СвНомТел = СвНомТелТипCreate(item.find('СвНомТел'))
            self.СвРождФЛ = СвРождЕГРЮЛТипCreate(item.find('СвРождФЛ'))
            self.УдЛичнФЛ = УдЛичнЕГРЮЛТипCreate(item.find('УдЛичнФЛ'))
            self.АдресМЖРФ = АдрРФЕГРЮЛТипCreate(item.find('АдресМЖРФ'))
            self.АдрМЖИн = АдрИнЕГРЮЛТипCreate(item.find('АдрМЖИн'))
            self.СвДискв = СвДисквCreate(item.find('СвДискв'))


            self.a = СведДолжнФЛ.objects.create(ГРНДатаПерв=self.ГРНДатаПерв.save(), СвФЛ=self.СвФЛ.save(),
                                                СвДолжн=self.СвДолжн.save(), СвНомТел=self.СвНомТел.save(),
                                                СвРождФЛ=self.СвРождФЛ.save(), УдЛичнФЛ=self.УдЛичнФЛ.save(),
                                                АдресМЖРФ=self.АдресМЖРФ.save(), АдрМЖИн=self.АдрМЖИн.save(),
                                                СвДискв=self.СвДискв.save(),
                                                )
            self.СвНедДанУпрОрг = [СвНедДанДолжнФЛCreate(i) for i in item.findall('СвНедДанДолжнФЛ')]
            for one_СвНедДанДолжнФЛ in item.findall('СвНедДанДолжнФЛ'):
                self.a.СвН.add(СвНедДанДолжнФЛCreate(one_СвНедДанДолжнФЛ).save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
