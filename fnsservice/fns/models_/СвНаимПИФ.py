from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate


class СвНаимПИФ(models.Model): #4.48
    СвНаимПИФ = models.CharField(max_length=1000, null=True, verbose_name='Название (индивидуальное обозначение) паевого инвестиционного фонда')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвНаимПИФ_Дата', verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True, verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'СвНаимПИФ: %s' % (self.СвНаимПИФ,)


class СвНаимПИФCreate:

    def __init__(self, item):
        if item is not None:
            self.СвНаимПИФ = item.get('СвНаимПИФ')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвНаимПИФ.objects.create(СвНаимПИФ=self.СвНаимПИФ,
                                              ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a