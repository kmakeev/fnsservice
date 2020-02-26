from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвЮЛЕГРЮЛТип import СвЮЛЕГРЮЛТип, СвЮЛЕГРЮЛТипCreate
from .СвРегИнЮЛЕГРЮЛТип import СвРегИнЮЛЕГРЮЛТип, СвРегИнЮЛЕГРЮЛТипCreate
from .СвНотУдДогЗалТип import СвНотУдДогЗалТип, СвНотУдДогЗалТипCreate
from datetime import datetime


class СвЗалогДержЮЛ(models.Model): # 4.100

    ГРНДатаПерв = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                    verbose_name='ГРН и дата внесения в ЕГРЮЛ сведений о данном лице', on_delete=models.DO_NOTHING)

    НаимИННЮЛ = models.ForeignKey(СвЮЛЕГРЮЛТип, null=True, blank=True, verbose_name='Сведения о наименовании и (при наличии) ОГРН и ИНН ЮЛ', on_delete=models.DO_NOTHING)
    СвРегИн = models.ForeignKey(СвРегИнЮЛЕГРЮЛТип, null=True, blank=True,
                                  verbose_name='Сведения о регистрации в стране происхождения', on_delete=models.DO_NOTHING)
    СвНотУдДогЗал = models.ForeignKey(СвНотУдДогЗалТип, null=True, blank=True,
                                verbose_name='Сведения о нотариальном удостоверении договора залога', on_delete=models.DO_NOTHING)


    def __str__(self):
        return '%s - %s' % (self.ГРНДатаПерв, self.СвДолжн.__str__(),)


class СвЗалогДержЮЛCreate:

    def __init__(self, item):
        if item is not None:
            self.ГРНДатаПерв = ГРНДатаТипCreate(item.find('ГРНДатаПерв'))
            self.НаимИННЮЛ = СвЮЛЕГРЮЛТипCreate(item.find('НаимИННЮЛ'))
            self.СвРегИн = СвРегИнЮЛЕГРЮЛТипCreate(item.find('СвРегИн'))
            self.СвНотУдДогЗал = СвНотУдДогЗалТипCreate(item.find('СвНотУдДогЗал'))
            self.a = СвЗалогДержЮЛ.objects.create(ГРНДатаПерв=self.ГРНДатаПерв.save(),
                                                  НаимИННЮЛ=self.НаимИННЮЛ.save(), СвРегИн=self.СвРегИн.save(),
                                                  СвНотУдДогЗал=self.СвНотУдДогЗал.save())

        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a