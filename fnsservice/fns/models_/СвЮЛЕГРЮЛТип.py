from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from django.contrib.postgres.search import SearchVector, SearchVectorField
from django.contrib.postgres.indexes import GinIndex


class СвЮЛЕГРЮЛТип(models.Model): #4.107
    ОГРН = models.CharField(max_length=13, null=True,
                            verbose_name='Основной государственный регистрационный номер юридического лица')
    ИНН = models.CharField(max_length=10, null=True, verbose_name='ИНН юридического лица')
    НаимЮЛПолн = models.CharField(max_length=1000, null=True,
                                  verbose_name='Полное наименование юридического лица на русском языке')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвЮЛЕГРЮЛТип_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector']),
            models.Index(fields=['НаимЮЛПолн', 'ОГРН', 'ИНН'])
        ]

    def __str__(self):
        return '%s - %s ' % (self.ОГРН, self.НаимЮЛПолн,)


class СвЮЛЕГРЮЛТипCreate:

    def __init__(self, item):
        if item is not None:
            self.ОГРН = item.get('ОГРН')
            self.ИНН = item.get('ИНН')
            self.НаимЮЛПолн = item.get('НаимЮЛПолн')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвЮЛЕГРЮЛТип.objects.create(ОГРН=self.ОГРН, ИНН=self.ИНН, НаимЮЛПолн=self.НаимЮЛПолн,
                                                 ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a

