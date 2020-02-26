from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate


class СвРеоргЮЛ(models.Model): #4.59
    ОГРН = models.CharField(max_length=13, null=True, verbose_name='Основной государственный регистрационный номер юридического лица')
    ИНН = models.CharField(max_length=10, null=True,
                            verbose_name='ИНН юридического лица')
    НаимЮЛПолн = models.CharField(max_length=1000, null=True, verbose_name='Полное наименование юридического лица')
    СостЮЛпосле = models.CharField(max_length=50, null=True, verbose_name='Состояние юридического лица после завершения реорганизации')
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвРеоргЮЛ_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.ОГРН, self.НаимЮЛПолн,)


class СвРеоргЮЛCreate:

    def __init__(self, item):
        if item is not None:
            self.ОГРН = item.get('ОГРН')
            self.ИНН = item.get('ИНН')
            self.НаимЮЛПолн = item.get('НаимЮЛПолн')
            self.СостЮЛпосле = item.get('СостЮЛпосле')
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвРеоргЮЛ.objects.create(ОГРН=self.ОГРН, ИНН=self.ИНН, НаимЮЛПолн=self.НаимЮЛПолн,
                                              СостЮЛпосле=self.СостЮЛпосле, ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
