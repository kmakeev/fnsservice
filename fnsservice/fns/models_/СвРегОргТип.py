from django.db import models


class СвРегОргТип(models.Model): #4.103
    КодНО = models.CharField(max_length=4,
                                verbose_name='Код органа по справочнику СОУН')
    НаимНО = models.CharField(max_length=250,
                             verbose_name='Наименование регистрирующего (налогового) органа')

    def __str__(self):
        return '%s - %s' % (self.КодНО, self.НаимНО,)


class СвРегОргТипCreate:

    def __init__(self, item):
        if item is not None:

            self.КодНО = item.get('КодНО')
            self.НаимНО = item.get('НаимНО')

            self.a = СвРегОргТип.objects.create(КодНО=self.КодНО, НаимНО=self.НаимНО)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
