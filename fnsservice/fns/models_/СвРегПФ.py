from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвОргПФ import СвОргПФ, СвОргПФCreate
from datetime import datetime


class СвРегПФ(models.Model): #4.19
    РегНомПФ = models.CharField(max_length=15, null=True, verbose_name='Регистрационный номер в территориальном органе Пенсионного фонда Российской Федерации')
    ДатаРег = models.DateField(auto_now=False, null=True, auto_now_add=False,
                                  verbose_name='Дата регистрации юридического лица в качестве страхователя')
    СвОргПФ = models.ForeignKey(СвОргПФ, null=True, blank=True,
                                  verbose_name='Сведения о территориальном органе Пенсионного фонда Российской Федерации', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвРегПФ_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s № %s' % (self.ДатаРег, self.РегНомПФ,)


class СвРегПФCreate:

    def __init__(self, item):
        if item is not None:
            self.РегНомПФ = item.get('РегНомПФ')
            self.ДатаРег = item.get('ДатаРег')
            self.СвОргПФ = СвОргПФCreate(item.find('СвОргПФ'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвРегПФ.objects.create(РегНомПФ=self.РегНомПФ, ДатаРег=datetime.strptime(self.ДатаРег, '%Y-%m-%d'),
                                            СвОргПФ=self.СвОргПФ.save(),
                                            ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
