from django.db import models


class НаселПунктТип(models.Model): # 4.89

    ТипНаселПункт = models.CharField(max_length=30, null=True,
                                  verbose_name='Тип элемента населенный пункт (поселок, село и т.п.)')
    НаимНаселПункт = models.CharField(max_length=255, null=True,
                                verbose_name='Наименование (элемент населенный пункт)')

    class Meta:
        indexes = [
            models.Index(fields=['ТипНаселПункт', 'НаимНаселПункт', ])
        ]

    def __str__(self):
        return ' %s %s' % (self.ТипНаселПункт, self.НаимНаселПункт,)


class НаселПунктТипCreate:

    def __init__(self, item):
        if item is not None:
            self.ТипНаселПункт = item.get('ТипНаселПункт')
            self.НаимНаселПункт = item.get('НаимНаселПункт')

            self.a = НаселПунктТип.objects.create(ТипНаселПункт=self.ТипНаселПункт, НаимНаселПункт=self.НаимНаселПункт)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
