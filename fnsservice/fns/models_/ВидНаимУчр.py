from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate


class ВидНаимУчр(models.Model): #4.44

    КодУчрРФСубМО = models.CharField(max_length=1, null=True, verbose_name='Код вида учредителя')
    НаимМО = models.CharField(max_length=1000, null=True,
                                verbose_name='Наименование вида должностного лица по справочнику СКФЛЮЛ')
    КодРегион = models.CharField(max_length=2, null=True, verbose_name='Код субъекта Российской Федерации, который является учредителем (участником) юридического лица или на территории которого находится муниципальное образование, которое является учредителем (участником) юридического лица')
    НаимРегион = models.CharField(max_length=100, null=True,
                              verbose_name='Наименование субъекта Российской Федерации')

    def __str__(self):
        return '%s - %s ' % (self.КодУчрРФСубМО, self.ННаимМО,)


class ВидНаимУчрCreate:

    def __init__(self, item):
        if item is not None:
            self.КодУчрРФСубМО = item.get('КодУчрРФСубМО')
            self.НаимМО = item.get('НаимМО')
            self.КодРегион = item.get('КодРегион')
            self.НаимРегион = item.get('НаимРегион')

            self.a = ВидНаимУчр.objects.create(КодУчрРФСубМО=self.КодУчрРФСубМО, НаимМО=self.НаимМО,
                                               КодРегион=self.КодРегион, НаимРегион=self.НаимРегион)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a