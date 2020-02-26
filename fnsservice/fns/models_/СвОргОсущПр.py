from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвФЛЕГРЮЛТип import СвФЛЕГРЮЛТип, СвФЛЕГРЮЛТипCreate


class СвОргОсущПр(models.Model): #4.45

    ГРНДатаПерв = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ сведений о данном лице', on_delete=models.DO_NOTHING)
    НаимИННЮЛ = models.ForeignKey(СвФЛЕГРЮЛТип, null=True, blank=True,
                                 verbose_name='Сведения о наименовании и (при наличии) ОГРН и ИНН органа государственной власти, органа местного самоуправления или ЮЛ', on_delete=models.DO_NOTHING)



    def __str__(self):
        return '%s - %s' % (self.ГРНДатаПерв, self.НаимИННЮЛ.__str__(),)


class СвОргОсущПрCreate:

    def __init__(self, item):
        if item is not None:
            self.ГРНДатаПерв = ГРНДатаТипCreate(item.find('ГРНДатаПерв'))
            self.НаимИННЮЛ = СвФЛЕГРЮЛТипCreate(item.find('СвФЛ'))

            self.a = СвОргОсущПр.objects.create(ГРНДатаПерв=self.ГРНДатаПерв.save(),
                                                НаимИННЮЛ=self.НаимИННЮЛ.save())

        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a