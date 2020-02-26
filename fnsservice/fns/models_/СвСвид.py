from django.db import models
from datetime import datetime
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate


class СвСвид(models.Model): #4.78
    Серия = models.CharField(max_length=2, null=True, verbose_name='Серия бланка свидетельства')
    Номер = models.CharField(max_length=255, null=True, verbose_name='Номер документа')
    ДатаВыдСвид = models.DateField(auto_now=False, null=True, auto_now_add=False,
                               verbose_name='Дата документа')
    ГРНДатаСвидНед = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                       verbose_name='ГРН и дата записи, которая признана недействительной', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.ДатаДок, self.НаимДок,)


class СвСвидCreate:
    def __init__(self, item):
        if item is not None:
            self.Серия = item.get('Серия')
            self.Номер = item.get('Номер')
            self.ДатаВыдСвид = item.get('ДатаВыдСвид')
            self.ГРНДатаСвидНед = ГРНДатаТипCreate(item.find('ГРНДатаСвидНед'))
            self.a = СвСвид.objects.create(Серия=self.Серия, Номер=self.Номер,
                                                ДатаВыдСвид=datetime.strptime(self.ДатаВыдСвид, '%Y-%m-%d'),
                                                ГРНДатаСвидНед=self.ГРНДатаСвидНед.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a