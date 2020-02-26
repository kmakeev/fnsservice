from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .РешСудТип import РешСудТип, РешСудТипCreate


class СвНедДанДолжнФЛ(models.Model): #4.33

    ПризнНедДанДолжнФЛ = models.CharField(max_length=1, null=True,
                                  verbose_name='Признак недостоверности данных')
    ТекстНедДанДолжнФЛ = models.CharField(max_length=500, null=True,
                              verbose_name='Текст о недостоверности сведений, выводимый в выписке в строке с наименованием «Дополнительные сведения»')
    РешСудНедДанДолжнФЛ = models.ForeignKey(РешСудТип, null=True, blank=True,
                                    verbose_name='Сведения о решении суда, на основании которого указанные сведения признаны недостоверными', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвНедДанДолжнФЛ_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s ' % (self.ОГРНИП, self.НаимДолжн,)


class СвНедДанДолжнФЛCreate:

    def __init__(self, item):
        if item is not None:
            self.ПризнНедДанДолжнФЛ = item.get('ПризнНедДанДолжнФЛ')
            self.ТекстНедДанДолжнФЛ = item.get('ТекстНедДанДолжнФЛ')
            self.РешСудНедДанДолжнФЛ = РешСудТипCreate(item.find('РешСудНедДанДолжнФЛ'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвНедДанДолжнФЛ.objects.create(ПризнНедДанДолжнФЛ=self.ПризнНедДанДолжнФЛ, ТекстНедДанДолжнФЛ=self.ТекстНедДанДолжнФЛ,
                                                    РешСудНедДанДолжнФЛ=self.РешСудНедДанДолжнФЛ.save(),
                                                    ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
