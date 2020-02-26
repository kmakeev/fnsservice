from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвЮЛЕГРЮЛТип import СвЮЛЕГРЮЛТип, СвЮЛЕГРЮЛТипCreate


class СвУпрКомпПИФ(models.Model): #4.49
    ГРНДатаПерв = models.ForeignKey(ГРНДатаТип, null=True, blank=True,  verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    УпрКомпПиф = models.ForeignKey(СвЮЛЕГРЮЛТип, null=True, blank=True, verbose_name='Наименование и (при наличии) ОГРН и ИНН управляющей компании паевого инвестиционного фонда', on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'СвНаимПИФ: %s' % (self.СвНаимПИФ,)


class СвУпрКомпПИФCreate:

    def __init__(self, item):
        if item is not None:

            self.ГРНДатаПерв = ГРНДатаТипCreate(item.find('ГРНДатаПерв'))
            self.УпрКомпПиф = СвЮЛЕГРЮЛТипCreate(item.find('УпрКомпПиф'))

            self.a = СвУпрКомпПИФ.objects.create(ГРНДатаПерв=self.ГРНДатаПерв.save(), УпрКомпПиф=self.УпрКомпПиф.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
