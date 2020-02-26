from django.db import models
from .ДробьТип import ДробьТип, ДробьТипCreate


class РазмерДоли(models.Model): #4.87
    Процент = models.FloatField(null=True, blank=True, verbose_name='Размер доли в процентах')
    ДробДесят = models.FloatField(null=True, blank=True, verbose_name='Размер доли в десятичных дробях')
    ДробПрост = models.ForeignKey(ДробьТип, null=True, blank=True,
                                  verbose_name='Размер доли в простых дробях', on_delete=models.DO_NOTHING)


class РазмерДолиCreate:

    def __init__(self, item):
        if item is not None:
            self.Процент = item.find('Процент')
            self.ДробДесят = item.find('ДробДесят')
            self.ДробПрост = ДробьТипCreate(item.find('ДробПрост'))
            self.a = РазмерДоли.objects.create(ДробПрост=self.ДробПрост.save())
            if self.ДробДесят is not None:
                self.a.ДробДесят = float(self.ДробДесят.text)
            if self.Процент is not None:
                self.a.Процент = float(self.Процент.text)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a

