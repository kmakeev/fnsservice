from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .РешСудТип import РешСудТип, РешСудТипCreate


class СвНедДанУпрОрг(models.Model):
    ПризнНедДанУпрОрг = models.CharField(max_length=1, null=True, blank=True,
                                  verbose_name='Признак недостоверности данных')
    ТекстНедДанУпрОрг = models.CharField(max_length=500, null=True, blank=True,
                                         verbose_name='Текст о недостоверности сведений, выводимый в выписке в строке с наименованием «Дополнительные сведения»')
    РешСудНедДанУпрОрг = models.ForeignKey(РешСудТип, null=True, blank=True,
                                verbose_name='Сведения о решении суда, на основании которого указанные сведения признаны недостоверными', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвНедДанУпрОрг_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s ' % (self.ПризнНедДанУпрОрг, self.ТекстНедДанУпрОрг,)


class СвНедДанУпрОргCreate:

    def __init__(self, item):
        if item is not None:
            self.ПризнНедДанУпрОрг = item.get('ПризнНедДанУпрОрг')
            self.ТекстНедДанУпрОрг = item.get('ТекстНедДанУпрОрг')
            self.РешСудНедДанУпрОрг = РешСудТипCreate(item.find('РешСудНедДанУпрОрг'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвНедДанУпрОрг.objects.create(ПризнНедДанУпрОрг=self.ПризнНедДанУпрОрг, ТекстНедДанУпрОрг=self.ТекстНедДанУпрОрг,
                                                   РешСудНедДанУпрОрг=self.РешСудНедДанУпрОрг.save(),
                                                   ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
