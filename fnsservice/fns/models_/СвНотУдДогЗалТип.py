from django.db import models
from .СвФЛЕГРЮЛТип import СвФЛЕГРЮЛТип, СвФЛЕГРЮЛТипCreate
from datetime import datetime


class СвНотУдДогЗалТип(models.Model): #4.97
    Номер = models.CharField(max_length=255, null=True, blank=True,
                              verbose_name='Номер договора залога')
    Дата = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='Дата договора залога')
    СвНотариус = models.ForeignKey(СвФЛЕГРЮЛТип, null=True, blank=True,
                                verbose_name='ФИО и (при наличии) ИНН нотариуса, удостоверившего договор залога', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s' % (self.Номер,)


class СвНотУдДогЗалТипCreate:
    def __init__(self, item):
        if item is not None:
            self.Номер = item.get('Номер')
            self.Дата = item.get('Дата')
            self.СвНотариус = СвФЛЕГРЮЛТипCreate(item.find('СвНотариус'))
            self.a = СвНотУдДогЗалТип.objects.create(Номер=self.Номер, Дата=datetime.strptime(self.Дата, '%Y-%m-%d'),
                                                     СвНотариус=self.СвНотариус.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
