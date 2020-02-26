from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвФЛЕГРЮЛТип import СвФЛЕГРЮЛТип, СвФЛЕГРЮЛТипCreate
from .СвРождЕГРЮЛТип import СвРождЕГРЮЛТип, СвРождЕГРЮЛТипCreate
from .УдЛичнЕГРЮЛТип import УдЛичнЕГРЮЛТип, УдЛичнЕГРЮЛТипCreate
from .АдрРФЕГРЮЛТип import АдрРФЕГРЮЛТип, АдрРФЕГРЮЛТипCreate
from .АдрИнЕГРЮЛТип import АдрИнЕГРЮЛТип, АдрИнЕГРЮЛТипCreate


class СвФЛОсущПр(models.Model): #4.46
    ГРНДатаПерв = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ сведений о данном лице', on_delete=models.DO_NOTHING)
    СвФЛ = models.ForeignKey(СвФЛЕГРЮЛТип, null=True, blank=True,
                                 verbose_name='Сведения о ФИО и (при наличии) ИНН ФЛ', on_delete=models.DO_NOTHING)
    СвРождФЛ = models.ForeignKey(СвРождЕГРЮЛТип, null=True, blank=True,
                                 verbose_name='Сведения о рождении ФЛ', on_delete=models.DO_NOTHING)
    УдЛичнФЛ = models.ForeignKey(УдЛичнЕГРЮЛТип, null=True, blank=True,
                                 verbose_name='Сведения о документе, удостоверяющем личность', on_delete=models.DO_NOTHING)
    АдресМЖРФ = models.ForeignKey(АдрРФЕГРЮЛТип, null=True, blank=True,
                                  verbose_name='Сведения об адресе места жительства в Российской Федерации', on_delete=models.DO_NOTHING)
    АдрМЖИн = models.ForeignKey(АдрИнЕГРЮЛТип, null=True, blank=True,
                                verbose_name='Сведения об адресе места жительства за пределами территории Российской Федерации', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.ГРНДатаПерв, self.СвФЛ.__str__(),)


class СвФЛОсущПрCreate:

    def __init__(self, item):
        if item is not None:
            self.ГРНДатаПерв = ГРНДатаТипCreate(item.find('ГРНДатаПерв'))
            self.СвФЛ = СвФЛЕГРЮЛТипCreate(item.find('СвФЛ'))
            self.СвРождФЛ = СвРождЕГРЮЛТипCreate(item.find('СвРождФЛ'))
            self.УдЛичнФЛ = УдЛичнЕГРЮЛТипCreate(item.find('УдЛичнФЛ'))
            self.АдресМЖРФ = АдрРФЕГРЮЛТипCreate(item.find('АдресМЖРФ'))
            self.АдрМЖИн = АдрИнЕГРЮЛТипCreate(item.find('АдрМЖИн'))

            self.a = СвФЛОсущПр.objects.create(ГРНДатаПерв=self.ГРНДатаПерв.save(),
                                          СвФЛ=self.СвФЛ.save(),
                                          СвРождФЛ=self.СвРождФЛ.save(),
                                          УдЛичнФЛ=self.УдЛичнФЛ.save(),
                                          АдресМЖРФ=self.АдресМЖРФ.save(),
                                          АдрМЖИн=self.АдрМЖИн.save())

        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
