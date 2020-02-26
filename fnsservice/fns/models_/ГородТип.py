from django.db import models


class ГородТип(models.Model): # 4.83
    ТипГород = models.CharField(max_length=30, null=True,
                                  verbose_name='Тип элемента город (город, волость и т.п.)')
    НаимГород = models.CharField(max_length=40, null=True,
                                verbose_name='Наименование (элемент город) ')

    class Meta:
        indexes = [
            models.Index(fields=['ТипГород', 'НаимГород', ])
        ]

    def __str__(self):
        return ' %s %s' % (self.ТипГород, self.НаимГород,)


class ГородТипCreate:
    def __init__(self, city):
        if city is not None:
            self.ТипГород = city.get('ТипГород')
            self.НаимГород = city.get('НаимГород')
            self.a = ГородТип.objects.create(ТипГород=self.ТипГород, НаимГород=self.НаимГород)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a

