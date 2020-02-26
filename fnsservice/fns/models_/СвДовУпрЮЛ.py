from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвЮЛЕГРЮЛТип import СвЮЛЕГРЮЛТип, СвЮЛЕГРЮЛТипCreate


class СвДовУпрЮЛ(models.Model): # 4.40
    ГРНДатаПерв = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ сведений о данном лице', on_delete=models.DO_NOTHING)
    НаимИННДовУпр = models.ForeignKey(СвЮЛЕГРЮЛТип, null=True, blank=True,
                                verbose_name='Сведения о наименовании и (при наличии) ОГРН и ИНН ЮЛ', on_delete=models.DO_NOTHING)


    def __str__(self):
        return '%s - %s ' % (self.ГРНДатаПерв.__str__(), self.НаимИННДовУпр.__str__(),)


class СвДовУпрЮЛCreate:

    def __init__(self, item):
        if item is not None:
            self.ГРНДатаПерв = ГРНДатаТипCreate(item.find('ГРНДатаПерв'))
            self.НаимИННДовУпр = СвЮЛЕГРЮЛТипCreate(item.find('НаимИННДовУпр'))
            self.a = СвДовУпрЮЛ.objects.create(ГРНДатаПерв=self.ГРНДатаПерв.save(),
                                               НаимИННДовУпр=self.НаимИННДовУпр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
