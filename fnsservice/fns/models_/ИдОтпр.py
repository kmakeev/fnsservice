from django.db import models
from .ФИОТип import ФИОТип, ФИОТипCreate


class ИдОтпр(models.Model): #4.2
    ДолжОтв = models.CharField(max_length=100, blank=True, null=True, verbose_name='Должность ответственного лица')
    Тлф = models.CharField(max_length=20, blank=True, null=True, verbose_name='Номер контактного телефона')
    email = models.CharField(max_length=45, blank=True, null=True, verbose_name='E-mail')
    ФИООтв = models.ForeignKey(ФИОТип, null=True, blank=True, verbose_name='Сведения об отправителе', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s' % self.ФИООтв


class ИдОтпрCreate:

    def __init__(self, item):
        if item is not None:
            self.ДолжОтв = item.get('ДолжОтв')
            self.Тлф = item.get('Тлф')
            self.email = item.get('email')
            self.ФИООтв = ФИОТипCreate(item.find('ФИООтв'))

            self.a = ИдОтпр.objects.create(ДолжОтв=self.ДолжОтв, Тлф=self.Тлф,
                                           email=self.email, ФИООтв=self.ФИООтв.save())
        self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
