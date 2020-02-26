from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from datetime import datetime
from .СпПрекрЮЛ import СпПрекрЮЛ, СпПрекрЮЛCreate
from .СвРегОргТип import СвРегОргТип, СвРегОргТипCreate
from rest_framework import serializers

class СвПрекрЮЛ(models.Model): #4.16
    ДатаПрекрЮЛ = models.DateField(auto_now=False, auto_now_add=False, null=True,
                               verbose_name='Дата прекращения юридического лица')
    СпПрекрЮЛ = models.ForeignKey(СпПрекрЮЛ, null=True, blank=True,
                                 verbose_name='Способ прекращения юридического лица', on_delete=models.DO_NOTHING)
    СвРегОрг = models.ForeignKey(СвРегОргТип, null=True, blank=True,
                                 verbose_name='Сведения о регистрирующем (налоговом) органе, внесшем запись о прекращении юридического лица', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвПрекрЮЛ_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.ДатаПрекрЮЛ, self.СпПрекрЮЛ.__str__,)


class СвПрекрЮЛCreate:

    def __init__(self, item):
        if item is not None:
            self.ДатаПрекрЮЛ = item.get('ДатаПрекрЮЛ')
            self.СпПрекрЮЛ = СпПрекрЮЛCreate(item.find('СпПрекрЮЛ'))
            self.СвРегОрг = СвРегОргТипCreate(item.find('СвРегОрг'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))

            self.a = СвПрекрЮЛ.objects.create(ДатаПрекрЮЛ=datetime.strptime(self.ДатаПрекрЮЛ, '%Y-%m-%d'),
                                              СпПрекрЮЛ=self.СпПрекрЮЛ.save(), СвРегОрг=self.СвРегОрг.save(),
                                              ГРНДата=self.ГРНДата.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a


class СвПрекрЮЛSerializer(serializers.ModelSerializer):

    class Meta:
        model = СвПрекрЮЛ
        fields = ('ДатаПрекрЮЛ',)

