from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate


class СвСтатусЗап(models.Model): #4.79

    ГРНДатаНед = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвСтатусЗап_Дата',
                                       verbose_name='ГРН и дата внесения записи, которой запись признана недействительной', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                       verbose_name='ГРН и дата записи, которой внесены исправления в связи с технической ошибкой', on_delete=models.DO_NOTHING)


class СвСтатусЗапCreate:
    def __init__(self, item):
        if item is not None:

            self.ГРНДатаНед = ГРНДатаТипCreate(item.find('ГРНДатаНед'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))
            self.a = СвСтатусЗап.objects.create(ГРНДатаНед=self.ГРНДатаНед.save(),
                                                ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a