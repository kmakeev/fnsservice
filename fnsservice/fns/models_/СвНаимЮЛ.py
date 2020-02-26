from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVector, SearchVectorField
from rest_framework import serializers

def vector():
    return SearchVector('НаимЮЛПолн', 'НаимЮЛСокр', config='russian')

class СвНаимЮЛ(models.Model): #4.5
    НаимЮЛПолн = models.CharField(max_length=1000, null=True, verbose_name='Полное наименование юридического лица на русском языке')
    НаимЮЛСокр = models.CharField(max_length=510, null=True, verbose_name='Сокращенное наименование юридического лица на русском языке')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвНаимЮЛ_Дата', verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True, verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector']),
            models.Index(fields=['НаимЮЛПолн', 'НаимЮЛСокр'])
            ]

    def __str__(self):
        return 'СвНаимЮЛ: %s' % (self.НаимЮЛСокр,)


class СвНаимЮЛCreate:

    def __init__(self, item):
        if item is not None:
            self.НаимЮЛПолн = item.get('НаимЮЛПолн')
            self.НаимЮЛСокр = item.get('НаимЮЛСокр')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвНаимЮЛ.objects.create(НаимЮЛПолн=self.НаимЮЛПолн, НаимЮЛСокр=self.НаимЮЛСокр,
                                             ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
            self.a.search_vector = vector()
            self.a.save()
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a


class СвНаимЮЛSerializer(serializers.ModelSerializer):

    class Meta:
        model = СвНаимЮЛ
        fields = ('НаимЮЛПолн', 'НаимЮЛСокр')
