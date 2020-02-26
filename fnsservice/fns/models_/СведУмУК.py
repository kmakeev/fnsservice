from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from datetime import datetime


class СведУмУК(models.Model): #4.24
    ВелУмУК = models.CharField(max_length=20, blank=True, null=True, verbose_name='Величина, на которую уменьшается уставный капитал (в рублях)')
    ДатаРеш = models.DateField(auto_now=False, null=True, auto_now_add=False,
                               verbose_name='Дата принятия решения об уменьшении уставного капитала')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СведУмУК_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s ' % (self.ДатаРеш, self.ВелУмУК,)


class СведУмУКCreate:

    def __init__(self, item):
        if item is not None:
            self.ВелУмУК = item.get('ВелУмУК')
            self.ДатаРеш = item.get('ДатаРеш')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СведУмУК.objects.create(ВелУмУК=self.ВелУмУК,
                                             ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
            if self.ДатаРеш is not None:
                self.a.ДатаРеш = datetime.strptime(self.ДатаРеш, '%Y-%m-%d')
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
