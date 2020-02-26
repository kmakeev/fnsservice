from django.db import models
from datetime import datetime


class СведПредДок(models.Model): #4.77
    НаимДок = models.CharField(max_length=255, null=True, verbose_name='Наименование документа')
    НомДок = models.CharField(max_length=255, null=True, verbose_name='Номер документа')
    ДатаДок = models.DateField(auto_now=False, null=True, auto_now_add=False,
                               verbose_name='Дата документа')

    def __str__(self):
        return '%s - %s' % (self.ДатаДок, self.НаимДок,)


class СведПредДокCreate:
    def __init__(self, item):
        if item is not None:
            self.НаимДок = item.find('НаимДок').text
            self.НомДок = item.find('НомДок')
            self.ДатаДок = item.find('ДатаДок')

            self.a = СведПредДок.objects.create(НаимДок=self.НаимДок)

            if self.ДатаДок is not None:
                self.a.ДатаДок = datetime.strptime(self.ДатаДок.text, '%Y-%m-%d')
            if self.НомДок is not None:
                self.a.НомДок = self.НомДок.text
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
