from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate


class СвДолжн(models.Model): #4.32

    ОГРНИП = models.CharField(max_length=15, null=True,
                                  verbose_name='Основной государственный регистрационный номер индивидуального предпринимателя - управляющего юридическим лицом')
    ВидДолжн = models.CharField(max_length=2, null=True,
                              verbose_name='Вид должностного лица по справочнику СКФЛЮЛ (указывается код по справочнику)')
    НаимВидДолжн = models.CharField(max_length=1000, null=True,
                                verbose_name='Наименование вида должностного лица по справочнику СКФЛЮЛ')
    НаимДолжн = models.CharField(max_length=1000, null=True,
                                    verbose_name='Наименование должности')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвДолжн_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s ' % (self.ОГРНИП, self.НаимДолжн,)


class СвДолжнCreate:

    def __init__(self, item):
        if item is not None:
            self.ОГРНИП = item.get('ОГРНИП')
            self.ВидДолжн = item.get('ВидДолжн')
            self.НаимВидДолжн = item.get('НаимВидДолжн')
            self.НаимДолжн = item.get('НаимДолжн')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвДолжн.objects.create(ОГРНИП=self.ОГРНИП, ВидДолжн=self.ВидДолжн,
                                            НаимВидДолжн=self.НаимВидДолжн, НаимДолжн=self.НаимДолжн,
                                            ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a