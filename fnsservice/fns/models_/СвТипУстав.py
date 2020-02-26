from django.db import models
from . СвНПАУтвТУ import СвНПАУтвТУ, СвНПАУтвТУCreate
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate


class СвТипУстав(models.Model): #4.25
    СвНПАУтвТУ = models.ForeignKey(СвНПАУтвТУ, null=True, blank=True,
                                  verbose_name='Сведения о нормативном правовом акте об утверждении типового устава ', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвТипУстав_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s' % (self.СвНПАУтвТУ.__str__,)


class СвТипУставCreate:

    def __init__(self, item):
        if item is not None:
            self.СвНПАУтвТУ = СвНПАУтвТУCreate(item.find('СвНПАУтвТУ'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвТипУстав.objects.create(СвНПАУтвТУ=self.СвНПАУтвТУ.save(), ГРНДата=self.ГРНДата.save(),
                                                 ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a