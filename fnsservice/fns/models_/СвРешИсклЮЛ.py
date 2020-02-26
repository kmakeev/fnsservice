from django.db import models
from datetime import datetime


class СвРешИсклЮЛ(models.Model): #4.15
    ДатаРеш = models.DateField(auto_now=False, auto_now_add=False, null=True,
                               verbose_name='Дата решения')
    НомерРеш = models.CharField(max_length=255,
                             verbose_name='Номер решения')
    ДатаПубликации = models.DateField(auto_now=False, auto_now_add=False, null=True,
                               verbose_name='Дата публикации решения ')
    НомерЖурнала = models.CharField(max_length=50,
                                verbose_name='Номер журнала, в котором опубликовано решение')

    def __str__(self):
        return '%s - %s' % (self.ДатаРеш, self.НомерРеш,)


class СвРешИсклЮЛCreate:

    def __init__(self, item):
        if item is not None:
            self.ДатаРеш = item.get('ДатаРеш')
            self.НомерРеш = item.get('НомерРеш')
            self.ДатаПубликации = item.get('ДатаПубликации')
            self.НомерЖурнала = item.get('НомерЖурнала')

            self.a = СвРешИсклЮЛ.objects.create(ДатаРеш=datetime.strptime(self.ДатаРеш, '%Y-%m-%d'),
                                                НомерРеш=self.НомерРеш, ДатаПубликации=datetime.strptime(self.ДатаПубликации, '%Y-%m-%d'),
                                                НомерЖурнала=self.НомерЖурнала)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
