from django.db import models
from . ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate


class СвНомТелТип(models.Model): #4.95
    НомТел = models.CharField(max_length=50, null=True, blank=True,
                              verbose_name='Контактный телефон')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвНомТелТип_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s' % (self.НомТел,)


class СвНомТелТипCreate:
    def __init__(self, item):
        if item is not None:
            self.НомТел = item.get('НомТел')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))
            self.a = СвНомТелТип.objects.create(НомТел=self.НомТел, ГРНДата=self.ГРНДата.save(),
                                                ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
