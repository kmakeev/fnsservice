from django.db import models
from datetime import datetime
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate


class СвРождЕГРЮЛТип(models.Model):  # 4.104
    ДатаРожд = models.DateField(auto_now=False, null=True, auto_now_add=False,
                               verbose_name='Дата рождения')
    МестоРожд = models.CharField(max_length=255, null=True, blank=True,
                                verbose_name='Место рождения')
    ПрДатаРожд = models.CharField(max_length=1, null=True, blank=True,
                                verbose_name='Признак полноты представляемой даты рождения физического лица')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвРождЕГРЮЛТип_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s, %s, ' % (self.ДатаРожд, self.МестоРожд, )


class СвРождЕГРЮЛТипCreate:

    def __init__(self, item):
        if item is not None:
            self.ДатаРожд = item.get('ДатаРожд')
            self.МестоРожд = item.get('МестоРожд')
            self.ПрДатаРожд = item.get('ПрДатаРожд')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвРождЕГРЮЛТип.objects.create(ДатаРожд=datetime.strptime(self.ДатаРожд, '%Y-%m-%d'), МестоРожд=self.МестоРожд, ПрДатаРожд=self.ПрДатаРожд,
                                                  ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
