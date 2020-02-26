from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate


class СвРегОрг(models.Model): #4.12
    КодНО = models.CharField(max_length=4, verbose_name='Код органа по справочнику СОУН')
    НаимНО = models.CharField(max_length=250, verbose_name='Наименование регистрирующего (налогового) органа')
    АдрРО = models.CharField(max_length=128, verbose_name='Адрес регистрирующего органа')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвРегОрг_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.КодНО, self.НаимНО,)


class СвРегОргCreate:

    def __init__(self, item):
        if item is not None:
            self.КодНО = item.get('КодНО')
            self.НаимНО = item.get('НаимНО')
            self.АдрРО = item.get('АдрРО')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))

            self.a = СвРегОрг.objects.create(КодНО=self.КодНО, НаимНО=self.НаимНО, АдрРО=self.АдрРО,
                                             ГРНДата=self.ГРНДата.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
