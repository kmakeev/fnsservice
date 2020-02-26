from django.db import models
from datetime import datetime
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate


class УдЛичнЕГРЮЛТип(models.Model):  # 4.108
    КодВидДок = models.CharField(max_length=2, null=True, blank=True,
                                  verbose_name='Код вида документа по справочнику СПДУЛ ')
    НаимДок = models.CharField(max_length=150, null=True, blank=True,
                                 verbose_name='Наименование вида документа')
    СерНомДок = models.CharField(max_length=50, null=True, blank=True,
                                 verbose_name='Серия и номер документа')
    ДатаДок = models.DateField(auto_now=False, null=True, auto_now_add=False,
                                verbose_name='Дата выдачи')
    ВыдДок = models.CharField(max_length=1000, null=True, blank=True,
                                 verbose_name='Серия и номер документа')
    КодВыдДок = models.CharField(max_length=7, null=True, blank=True,
                                 verbose_name='Код подразделения')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='УдЛичнЕГРЮЛТип_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.СерНомДок, self.НаимДок,)


class УдЛичнЕГРЮЛТипCreate:

    def __init__(self, item):
        if item is not None:
            self.КодВидДок = item.get('КодВидДок')
            self.НаимДок = item.get('НаимДок')
            self.СерНомДок = item.get('СерНомДок')
            self.ДатаДок = item.get('ДатаРожд')
            self.ВыдДок = item.get('ВыдДок')
            self.КодВыдДок = item.get('КодВыдДок')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = УдЛичнЕГРЮЛТип.objects.create(КодВидДок=self.КодВидДок, НаимДок=self.НаимДок, СерНомДок=self.СерНомДок,
                                                   ДатаДок=datetime.strptime(self.ДатаДок, '%Y-%m-%d'),
                                                   ВыдДок=self.ВыдДок, КодВыдДок=self.КодВыдДок,
                                                   ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a