from django.db import models


class СпПрекрЮЛ(models.Model): #4.17
    КодСпПрекрЮЛ = models.CharField(max_length=3, null=True, blank=True,
                                verbose_name='Код способа прекращения по справочнику СЮЛПД')
    НаимСпПрекрЮЛ = models.CharField(max_length=255, null=True, blank=True,
                                    verbose_name='Наименование способа прекращения')

    def __str__(self):
        return '%s - %s' % (self.КодСпПрекрЮЛ, self.НаимСпПрекрЮЛ,)


class СпПрекрЮЛCreate:

    def __init__(self, item):
        if item is not None:
            self.КодСпПрекрЮЛ = item.get('КодСпПрекрЮЛ')
            self.НаимСпПрекрЮЛ = item.get('НаимСпПрекрЮЛ')

            self.a = СпПрекрЮЛ.objects.create(КодСпПрекрЮЛ=self.КодСпПрекрЮЛ, НаимСпПрекрЮЛ=self.НаимСпПрекрЮЛ)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
