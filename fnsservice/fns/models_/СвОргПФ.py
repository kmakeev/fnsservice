from django.db import models


class СвОргПФ(models.Model): # 4.20
    КодПФ = models.CharField(max_length=6,
                             verbose_name='Код по справочнику СТОПФ')
    НаимПФ = models.CharField(max_length=255,
                          verbose_name='Наименование')

    def __str__(self):
        return '%s - %s' % (self.КодПФ, self.НаимПФ,)


class СвОргПФCreate:

    def __init__(self, item):
        if item is not None:
            self.КодПФ = item.get('КодПФ')
            self.НаимПФ = item.get('НаимПФ')

            self.a = СвОргПФ.objects.create(КодПФ=self.КодПФ, НаимПФ=self.НаимПФ)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a