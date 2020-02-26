from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from datetime import datetime
from .СпОбрЮЛ import СпОбрЮЛ, СпОбрЮЛCreate


class СвОбрЮЛ(models.Model): # 4.10
    ОГРН = models.CharField(max_length=13,
                            verbose_name='Основной государственный регистрационный номер юридического лица')
    ДатаОГРН = models.DateField(auto_now=False, null=True, auto_now_add=False, verbose_name='Дата присвоения ОГРН')
    РегНом = models.CharField(max_length=255, null=True, blank=True, verbose_name='Регистрационный номер, присвоенный российскому юридическому лицу до 1 июля 2002 года, или регистрационный номер юридического лица на территории Республики Крым или территории города федерального значения Севастополя на день принятия в РФ и образования в составе РФ новых субъектов - Республики Крым и города федерального значения Севастополя')
    ДатаРег = models.DateField(auto_now=False, null=True, blank=True, auto_now_add=False, verbose_name='Дата регистрации юридического лица')
    НаимРО = models.CharField(max_length=255, null=True, blank=True, verbose_name='Наименование органа, зарегистрировавшего юридическое лицо')
    СпОбрЮЛ = models.ForeignKey(СпОбрЮЛ, null=True, blank=True,
                                 verbose_name='Способ образования юридического лица ', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвОбрЮЛ_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.ДатаОГРН, self.ОГРН,)


class СвОбрЮЛCreate:

    def __init__(self, item):
        if item is not None:
            self.ОГРН = item.get('ОГРН')
            self.ДатаОГРН = item.get('ДатаОГРН')
            self.РегНом = item.get('РегНом')
            self.ДатаРег = item.get('ДатаРег')
            self.НаимРО = item.get('НаимРО')
            self.СпОбрЮЛ = СпОбрЮЛCreate(item.find('СпОбрЮЛ'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))
            # print(self.ОГРН, self.ДатаОГРН, self.РегНом, self.ДатаРег, self.НаимРО)
            self.a = СвОбрЮЛ.objects.create(ОГРН=self.ОГРН, ДатаОГРН=datetime.strptime(self.ДатаОГРН, '%Y-%m-%d'),
                                            РегНом=self.РегНом, НаимРО=self.НаимРО,
                                            СпОбрЮЛ=self.СпОбрЮЛ.save(), ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
            #if self.РегНом is not None:
            #    self.a.РегНом = self.РегНом
            if self.ДатаРег is not None:
                self.a.ДатаРег = datetime.strptime(self.ДатаРег, '%Y-%m-%d')
            #if self.НаимРО is not None:
            #    self.a.ДатаРег = self.НаимРО
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
