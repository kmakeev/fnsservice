from django.db import models


class РегионТип(models.Model): # 4.90
    ТипРегион = models.CharField(max_length=30, null=True,
                                  verbose_name='Тип элемента регион (республика, край и т.п.)')
    НаимРегион = models.CharField(max_length=40, null=True,
                                verbose_name='Наименование (элемент регион)')

    class Meta:
        indexes = [
            models.Index(fields=['ТипРегион', 'НаимРегион', ])
        ]

    def __str__(self):
        return ' %s %s' % (self.ТипРегион, self.НаимРегион,)


class РегионТипCreate:

    def __init__(self, item):
        if item is not None:
            self.ТипРегион = item.get('ТипРегион')
            self.НаимРегион = item.get('НаимРегион')
            self.a = РегионТип.objects.create(ТипРегион=self.ТипРегион, НаимРегион=self.НаимРегион)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
