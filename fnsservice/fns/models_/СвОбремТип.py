from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .РешСудТип import РешСудТип, РешСудТипCreate
from .СвЗалогДержФЛ import СвЗалогДержФЛ, СвЗалогДержФЛCreate
from .СвЗалогДержЮЛ import СвЗалогДержЮЛ, СвЗалогДержЮЛCreate


class СвОбремТип(models.Model): # 4.98
    ВидОбрем = models.CharField(max_length=16, null=True, blank=True,
                                  verbose_name='Вид обременения')
    СрокОбременения = models.CharField(max_length=5000, null=True, blank=True,
                                         verbose_name='Срок обременения или порядок определения срока')
    РешСуд = models.ForeignKey(РешСудТип, null=True, blank=True,
                                verbose_name='Сведения о решении судебного органа, по которому на долю учредителя (участника) наложено обременение', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвОбремТип_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)
    СвЗалогДержФЛ = models.ForeignKey(СвЗалогДержФЛ, null=True, blank=True,
                                verbose_name='Сведения о залогодержателе - ФЛ', on_delete=models.DO_NOTHING)
    СвЗалогДержЮЛ = models.ForeignKey(СвЗалогДержЮЛ, null=True, blank=True,
                                      verbose_name='Сведения о залогодержателе - ФЛ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s ' % (self.ПризнНедДанУпрОрг, self.ТекстНедДанУпрОрг,)


class СвОбремТипCreate:

    def __init__(self, item):
        if item is not None:
            self.ВидОбрем = item.get('ВидОбрем')
            self.СрокОбременения = item.get('СрокОбременения')
            self.РешСуд = РешСудТипCreate(item.find('РешСуд'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))
            self.СвЗалогДержФЛ = СвЗалогДержФЛCreate(item.find('СвЗалогДержФЛ'))
            self.СвЗалогДержЮЛ = СвЗалогДержЮЛCreate(item.find('СвЗалогДержЮЛ'))
            self.a = СвОбремТип.objects.create(ВидОбрем=self.ВидОбрем, СрокОбременения=self.СрокОбременения,
                                               РешСуд=self.РешСуд.save(),
                                               СвЗалогДержФЛ=self.СвЗалогДержФЛ.save(),
                                               СвЗалогДержЮЛ=self.СвЗалогДержЮЛ.save(),
                                               ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a