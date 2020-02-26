from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from datetime import datetime


class СвРегСтарые(models.Model): #4.37

    РегНом = models.CharField(max_length=255, null=True,
                                 verbose_name='Регистрационный номер, присвоенный юридическому лицу до 1 июля 2002 года')
    ДатаРег = models.DateField(auto_now=False, null=True, auto_now_add=False,
                               verbose_name='Дата регистрации юридического лица до 1 июля 2002 года')
    НаимРО = models.CharField(max_length=1000, null=True,
                              verbose_name='Наименование органа, зарегистрировавшего юридическое лицо до 1 июля 2002 года')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвРегСтарые_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                    verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s ' % (self.РегНом, self.НаимРО,)


class СвРегСтарыеCreate:

    def __init__(self, item):
        if item is not None:
            self.РегНом = item.get('РегНом')
            self.ДатаРег = item.get('ДатаРег')
            self.НаимРО = item.get('НаимРО')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвРегСтарые.objects.create(РегНом=self.РегНом,
                                                НаимРО=self.НаимРО,
                                                ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
            if self.ДатаРег is not None:
                self.a.ДатаРег = datetime.strptime(self.ДатаРег, '%Y-%m-%d')
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a

