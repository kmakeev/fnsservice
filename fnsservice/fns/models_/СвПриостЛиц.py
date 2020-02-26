from django.db import models
from . ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from datetime import datetime


class СвПриостЛиц(models.Model): #4.53
    ДатаПриостЛиц = models.DateField(auto_now=False, null=True, auto_now_add=False, verbose_name='Дата приостановления действия лицензии')
    ЛицОргПриостЛиц = models.CharField(max_length=1000, null=True, blank=True,
                                     verbose_name='Наименование лицензирующего органа, приостановившего действие лицензии')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвПриостЛиц_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.ДатаПриостЛиц, self.ЛицОргПриостЛиц,)


class СвПриостЛицCreate:
    def __init__(self, item):
        if item is not None:
            self.ДатаПриостЛиц = item.get('ДатаПриостЛиц')
            self.ЛицОргПриостЛиц = item.get('ЛицОргПриостЛиц')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвПриостЛиц.objects.create(ДатаПриостЛиц=datetime.strptime(self.ДатаПриостЛиц, '%Y-%m-%d'),
                                               ЛицОргПриостЛиц=self.ЛицОргПриостЛиц)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
