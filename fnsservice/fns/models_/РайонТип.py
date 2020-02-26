from django.db import models


class РайонТип(models.Model): # 4.90
    ТипРайон = models.CharField(max_length=30, null=True,
                                  verbose_name='Тип элемента район (район, улус и т.п.)')
    НаимРайон = models.CharField(max_length=40, null=True,
                                verbose_name='Наименование (элемент район) ')

    class Meta:
        indexes = [
            models.Index(fields=['ТипРайон', 'НаимРайон', ])
        ]

    def __str__(self):
        return ' %s %s' % (self.ТипРайон, self.НаимРайон,)


class РайонТипCreate:

    def __init__(self, item):
        if item is not None:
            self.ТипРайон = item.get('ТипРайон')
            self.НаимРайон = item.get('НаимРайон')

            self.a = РайонТип.objects.create(ТипРайон=self.ТипРайон, НаимРайон=self.НаимРайон)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a