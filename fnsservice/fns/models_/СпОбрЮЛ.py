from django.db import models


class СпОбрЮЛ(models.Model): # 4.11
    КодСпОбрЮЛ = models.CharField(max_length=2, null=True, verbose_name='Код способа образования по справочнику СЮЛНД')
    НаимСпОбрЮЛ = models.CharField(max_length=255, null=True, verbose_name='Наименование способа образования юридического лица')

    def __str__(self):
        return '%s - %s' % (self.КодСпОбрЮЛ, self.НаимСпОбрЮЛ,)


class СпОбрЮЛCreate:

    def __init__(self, item):
        if item is not None:
            self.КодСпОбрЮЛ = item.get('КодСпОбрЮЛ')
            self.НаимСпОбрЮЛ = item.get('НаимСпОбрЮЛ')

            self.a = СпОбрЮЛ.objects.create(КодСпОбрЮЛ=self.КодСпОбрЮЛ, НаимСпОбрЮЛ=self.НаимСпОбрЮЛ)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
