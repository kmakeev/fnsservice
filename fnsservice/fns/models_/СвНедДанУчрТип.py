from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .РешСудТип import РешСудТип, РешСудТипCreate


class СвНедДанУчрТип(models.Model): # 4.94
    ПризнНедДанУчр = models.CharField(max_length=1, null=True, blank=True,
                                  verbose_name='Признак недостоверности данных')
    ТекстНедДанУчр = models.CharField(max_length=500, null=True, blank=True,
                                         verbose_name='Текст о недостоверности сведений, выводимый в выписке в строке с наименованием «Дополнительные сведения»')
    РешСудНедДанУчр = models.ForeignKey(РешСудТип, null=True, blank=True,
                                verbose_name='Сведения о решении суда, на основании которого указанные сведения признаны недостоверными', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвНедДанУчрТип_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s ' % (self.ПризнНедДанУпрОрг, self.ТекстНедДанУпрОрг,)


class СвНедДанУчрТипCreate:

    def __init__(self, item):
        if item is not None:
            self.ПризнНедДанУчр = item.get('ПризнНедДанУчр')
            self.ТекстНедДанУчр = item.get('ТекстНедДанУчр')
            self.РешСудНедДанУчр = РешСудТипCreate(item.find('РешСудНедДанУчр'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвНедДанУчрТип.objects.create(ПризнНедДанУчр=self.ПризнНедДанУчр, ТекстНедДанУчр=self.ТекстНедДанУчр,
                                                   РешСудНедДанУчр=self.РешСудНедДанУчр.save(),
                                                   ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
