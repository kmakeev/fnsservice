from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from datetime import datetime


class СвРегИнЮЛЕГРЮЛТип(models.Model): # 4.102
    ОКСМ = models.CharField(max_length=3,
                             verbose_name='Код страны происхождения')
    НаимСтран = models.CharField(max_length=250, null=True, blank=True, verbose_name='Наименование страны происхождения')
    ДатаРег = models.DateField(auto_now=False, null=True, auto_now_add=False,
                               verbose_name='Дата регистрации')
    РегНомер = models.CharField(max_length=255, null=True, blank=True, verbose_name='Регистрационный номер')
    НаимРегОрг = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Наименование регистрирующего органа')
    АдрСтр = models.CharField(max_length=510, null=True, blank=True,
                                  verbose_name='Адрес (место нахождения) в стране происхождения')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвРегИн_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s ' % (self.ОКСМ, self.НаимСтран,)


class СвРегИнЮЛЕГРЮЛТипCreate:

    def __init__(self, item):
        if item is not None:
            self.ОКСМ = item.get('ОКСМ')
            self.НаимСтран = item.get('НаимСтран')
            self.ДатаРег = item.get('ДатаРег')
            self.РегНомер = item.get('РегНомер')
            self.НаимРегОрг = item.get('НаимРегОрг')
            self.АдрСтр = item.get('АдрСтр')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвРегИнЮЛЕГРЮЛТип.objects.create(ОКСМ=self.ОКСМ, НаимСтран=self.НаимСтран,
                                            РегНомер=self.РегНомер,  НаимРегОрг=self.НаимРегОрг, АдрСтр=self.АдрСтр,
                                            ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
            if self.ДатаРег is not None:
                self.a.ДатаРег = datetime.strptime(self.ДатаРег, '%Y-%m-%d')
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
