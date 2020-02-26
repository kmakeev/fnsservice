from django.db import models


class СвОргФСС(models.Model): #4.22
    КодФСС = models.CharField(max_length=4, verbose_name='Код по справочнику СТОПФ')
    НаимФСС = models.CharField(max_length=255, verbose_name='Наименование')

    def __str__(self):
        return '%s - %s' % (self.КодФСС, self.НаимФСС,)


class СвОргФССCreate:

    def __init__(self, item):
        if item is not None:
            self.КодФСС = item.get('КодФСС')
            self.НаимФСС = item.get('НаимФСС')

            self.a = СвОргФСС.objects.create(КодФСС=self.КодФСС, НаимФСС=self.НаимФСС)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a