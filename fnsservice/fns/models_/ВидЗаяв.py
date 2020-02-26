from django.db import models


class ВидЗаяв(models.Model): # 4.68
    КодСЗОЮЛ = models.CharField(max_length=4, null=True,
                                  verbose_name='Код по справочнику СЗОЮЛ')
    НаимСЗОЮЛ = models.CharField(max_length=500, null=True,
                                verbose_name='Наименование по справочнику СЗОЮЛ  ')

    def __str__(self):
        return ' %s %s' % (self.КодСПВЗ, self.НаимВидЗап,)


class ВидЗаявCreate:
    def __init__(self, item):
        if item is not None:
            self.КодСЗОЮЛ = item.get('КодСЗОЮЛ')
            self.НаимСЗОЮЛ = item.get('НаимСЗОЮЛ')

            self.a = ВидЗаяв.objects.create(КодСЗОЮЛ=self.КодСЗОЮЛ, НаимСЗОЮЛ=self.НаимСЗОЮЛ)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
