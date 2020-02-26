from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate


class СвПредЮЛ(models.Model): #4.29
    НаимПредЮЛ = models.CharField(max_length=500, null=True, blank=True,
                                         verbose_name='Полное наименование представительства или филиала в Российской Федерации, через которое иностранное ЮЛ осуществляет полномочия управляющей организации')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвПредЮЛ_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s' % (self.НаимПредЮЛ,)


class СвПредЮЛCreate:

    def __init__(self, item):
        if item is not None:
            self.НаимПредЮЛ = item.get('НаимПредЮЛ')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвПредЮЛ.objects.create(НаимПредЮЛ=self.НаимПредЮЛ,
                                             ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
