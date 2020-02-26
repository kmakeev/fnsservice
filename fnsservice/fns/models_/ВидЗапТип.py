from django.db import models


class ВидЗапТип(models.Model): # 4.80
    КодСПВЗ = models.CharField(max_length=5, null=True,
                                  verbose_name='Код вида записи (причины внесения записи в ЕГРЮЛ или ЕГРИП) по справочнику СПВЗ')
    НаимВидЗап = models.CharField(max_length=500, null=True,
                                verbose_name='Наименование вида записи (причины внесения записи в ЕГРЮЛ или ЕГРИП) ')

    def __str__(self):
        return ' %s %s' % (self.КодСПВЗ, self.НаимВидЗап,)


class ВидЗапТипCreate:
    def __init__(self, city):
        if city is not None:
            self.КодСПВЗ = city.get('КодСПВЗ')
            self.НаимВидЗап = city.get('НаимВидЗап')
            self.a = ВидЗапТип.objects.create(КодСПВЗ=self.КодСПВЗ, НаимВидЗап=self.НаимВидЗап)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
