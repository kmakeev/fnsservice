from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвОргФСС import СвОргФСС, СвОргФССCreate
from datetime import datetime


class СвРегФСС(models.Model): # 4.21
    РегНомФСС = models.CharField(max_length=15, null=True, verbose_name='Регистрационный номер в исполнительном органе Фонда социального страхования Российской Федерации')
    ДатаРег = models.DateField(auto_now=False, null=True, auto_now_add=False,
                               verbose_name='Дата регистрации юридического лица в качестве страхователя')
    СвОргФСС = models.ForeignKey(СвОргФСС, null=True, blank=True,
                                  verbose_name='Сведения об исполнительном органе Фонда социального страхования Российской Федерации', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвРегФСС_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s № %s' % (self.ДатаРег, self.РегНомФСС,)


class СвРегФССCreate:

    def __init__(self, item):
        if item is not None:
            self.РегНомФСС = item.get('РегНомФСС')
            self.ДатаРег = item.get('ДатаРег')
            self.СвОргПФ = СвОргФССCreate(item.find('СвОргФСС'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвРегФСС.objects.create(РегНомФСС=self.РегНомФСС, ДатаРег=datetime.strptime(self.ДатаРег, '%Y-%m-%d'),
                                             СвОргФСС=self.СвОргПФ.save(),
                                             ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
