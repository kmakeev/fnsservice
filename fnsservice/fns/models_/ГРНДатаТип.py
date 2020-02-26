from django.db import models
from datetime import datetime


class ГРНДатаТип (models.Model): #4.84
    ГРН = models.CharField(max_length=13, null=True, verbose_name='Государственный регистрационный номер записи ЕГРЮЛ')
    ДатаЗаписи = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='ДатаЗаписи')

    def __str__(self):
        return 'ГРН: %s, от %s' % (self.ГРН, self.ДатаЗаписи)


class ГРНДатаТипCreate:
    def __init__(self, grnDate):
        if grnDate is not None:
            self.ГРН = grnDate.get('ГРН')
            self.ДатаЗаписи = grnDate.get('ДатаЗаписи')
            self.a = ГРНДатаТип.objects.create(ГРН=self.ГРН)

            if self.ДатаЗаписи is not None:
                self.a.ДатаЗаписи = datetime.strptime(self.ДатаЗаписи, '%Y-%m-%d')
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a


