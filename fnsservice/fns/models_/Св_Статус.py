from django.db import models


class Св_Статус(models.Model): #4.14
    КодСтатусЮЛ = models.CharField(max_length=3,
                                verbose_name='Код статуса юридического лица по справочнику СЮЛСТ')
    НаимСтатусЮЛ = models.CharField(max_length=500,
                                   verbose_name='Наименование статуса юридического лица по справочнику СЮЛСТ')

    def __str__(self):
        return '%s - %s' % (self.КодСтатусЮЛ, self.НаимСтатусЮЛ,)


class Св_СтатусCreate:

    def __init__(self, item):
        if item is not None:
            self.КодСтатусЮЛ = item.get('КодСтатусЮЛ')
            self.НаимСтатусЮЛ = item.get('НаимСтатусЮЛ')

            self.a = Св_Статус.objects.create(КодСтатусЮЛ=self.КодСтатусЮЛ, НаимСтатусЮЛ=self.НаимСтатусЮЛ)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
