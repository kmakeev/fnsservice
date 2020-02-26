from django.db import models
from .СвРегОргТип import СвРегОргТип, СвРегОргТипCreate
from . ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СведПредДок import СведПредДок, СведПредДокCreate
from .СвСвид import СвСвид, СвСвидCreate
from .СвСтатусЗап import СвСтатусЗап, СвСтатусЗапCreate
from .ВидЗапТип import ВидЗапТип, ВидЗапТипCreate
from .СвЗаявФЛ import СвЗаявФЛ, СвЗаявФЛCreate
from datetime import datetime


class СвЗапЕГРЮЛ(models.Model): #4.66
    ИдЗап = models.CharField(max_length=19, null=True, blank=True,
                              verbose_name='Системный идентификатор записи')
    ГРН = models.CharField(max_length=13, null=True, blank=True,
                             verbose_name='Государственный регистрационный номер записи')
    ДатаЗап = models.DateField(auto_now=False, null=True, auto_now_add=False, verbose_name='Дата внесения записи в ЕГРЮЛ')
    ВидЗап = models.ForeignKey(ВидЗапТип, null=True, blank=True,
                                    verbose_name='Сведения о причине внесения записи в ЕГРЮЛ', on_delete=models.DO_NOTHING)
    СвРегОрг = models.ForeignKey(СвРегОргТип, null=True, blank=True,
                               verbose_name='Сведения о регистрирующем (налоговом) органе, внесшем запись в ЕГРЮЛ', on_delete=models.DO_NOTHING)
    СвРегОрг = models.ForeignKey(СвРегОргТип, null=True, blank=True,
                                 verbose_name='Сведения о регистрирующем (налоговом) органе, внесшем запись в ЕГРЮЛ', on_delete=models.DO_NOTHING)
    СвЗФЛ = models.ManyToManyField(СвЗаявФЛ,
                                     verbose_name='Сведения о заявителе')
    СведПредДок = models.ManyToManyField(СведПредДок,
                                      verbose_name='Сведения о документах, представленных при внесении записи в ЕГРЮЛ')
    СвСвид = models.ManyToManyField(СвСвид,
                                         verbose_name='Сведения о свидетельстве, подтверждающем факт внесения записи в ЕГРЮЛ')
    ГРНДатаИспрПред = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвЗапЕГРЮЛ_Дата',
                                verbose_name='ГРН и дата записи, в которую внесены исправления', on_delete=models.DO_NOTHING)
    ГРНДатаНедПред = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата записи, которая признана недействительной', on_delete=models.DO_NOTHING)
    СвСтатусЗап = models.ForeignKey(СвСтатусЗап, null=True, blank=True,
                                verbose_name='Сведения о статусе записи', on_delete=models.DO_NOTHING)

    class Meta:
        indexes = [
            models.Index(fields=['ГРН', 'ДатаЗап', ])
        ]

    def __str__(self):
        return '%s - %s' % (self.ДатаЛиц, self.НаимЛицВидДеят,)


class СвЗапЕГРЮЛCreate:
    def __init__(self, item):
        if item is not None:
            self.ИдЗап = item.get('ИдЗап')
            self.ГРН = item.get('ГРН')
            self.ДатаЗап = item.get('ДатаЗап')
            self.ВидЗап = ВидЗапТипCreate(item.find('ВидЗап'))
            self.СвРегОрг = СвРегОргТипCreate(item.find('СвРегОрг'))
            self.ГРНДатаИспрПред = ГРНДатаТипCreate(item.find('ГРНДатаИспрПред'))
            self.ГРНДатаНедПред = ГРНДатаТипCreate(item.find('ГРНДатаНедПред'))
            self.СвСтатусЗап = СвСтатусЗапCreate(item.find('СвСтатусЗап'))
            self.a = СвЗапЕГРЮЛ.objects.create(ИдЗап=self.ИдЗап, ГРН=self.ГРН,
                                               ДатаЗап=datetime.strptime(self.ДатаЗап, '%Y-%m-%d'),
                                               ВидЗап=self.ВидЗап.save(),
                                               СвРегОрг=self.СвРегОрг.save(),
                                               ГРНДатаИспрПред=self.ГРНДатаИспрПред.save(),
                                               ГРНДатаНедПред=self.ГРНДатаНедПред.save(),
                                               СвСтатусЗап=self.СвСтатусЗап.save())

            self.СвЗаявФЛ = [СвЗаявФЛCreate(i) for i in item.findall('СвЗаявФЛ')]
            for one_СвЗаявФЛ in self.СвЗаявФЛ:
                self.a.СвЗФЛ.add(one_СвЗаявФЛ.save())
            self.СведПредДок = [СведПредДокCreate(i) for i in item.findall('СведПредДок')]
            for one_СведПредДок in self.СведПредДок:
                self.a.СведПредДок.add(one_СведПредДок.save())
            self.СвСвид = [СвСвидCreate(i) for i in item.findall('СвСвид')]
            for one_СвСвид in self.СвСвид:
                self.a.СвСвид.add(one_СвСвид.save())

        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
