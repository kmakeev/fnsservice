from django.db import models


class УлицаТип(models.Model): # 4.109
    ТипУлица = models.CharField(max_length=30, null=True,
                                  verbose_name='Тип адресного объекта улица (улица, проспект, переулок и т.п.)')
    НаимУлица = models.CharField(max_length=255, null=True,
                                verbose_name='ННаименование (элемент улица) ')
    class Meta:
        indexes = [
            models.Index(fields=['ТипУлица', 'НаимУлица', ])
        ]

    def __str__(self):
        return ' %s %s' % (self.ТипУлица, self.НаимУлица,)


class УлицаТипCreate:

    def __init__(self, street):
        if street is not None:
            self.ТипУлица = street.get('ТипУлица')
            self.НаимУлица = street.get('НаимУлица')

            self.a = УлицаТип.objects.create(ТипУлица=self.ТипУлица, НаимУлица=self.НаимУлица)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
