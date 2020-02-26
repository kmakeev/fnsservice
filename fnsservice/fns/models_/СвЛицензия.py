from django.db import models
from . ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвПриостЛиц import СвПриостЛиц, СвПриостЛицCreate
from datetime import datetime
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVector, SearchVectorField

def vector():
    return SearchVector('НаимЛицВидДеят', config='russian')

class СвЛицензия(models.Model): #4.52
    НомЛиц = models.CharField(max_length=100, null=True, blank=True,
                              verbose_name='Серия и номер лицензии')
    ДатаЛиц = models.DateField(auto_now=False, null=True, auto_now_add=False, verbose_name='Дата лицензии')
    ДатаНачЛиц = models.DateField(auto_now=False, null=True, auto_now_add=False, verbose_name='Дата начала действия лицензии')
    ДатаОкончЛиц = models.DateField(auto_now=False, null=True, auto_now_add=False,
                                  verbose_name='Дата окончания действия лицензии')
    НаимЛицВидДеят = models.CharField(max_length=1000, null=True, blank=True,
                              verbose_name='Наименование лицензируемого вида деятельности, на который выдана лицензия')
    МестоДейстЛиц = models.CharField(max_length=1000, null=True, blank=True,
                                      verbose_name='Сведения об адресе места осуществления лицензируемого вида деятельности')
    ЛицОргВыдЛиц = models.CharField(max_length=1000, null=True, blank=True,
                                     verbose_name='Наименование лицензирующего органа, выдавшего или переоформившего лицензию')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвЛицензия_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)
    СвПриостЛиц = models.ForeignKey(СвПриостЛиц, null=True, blank=True,
                                verbose_name='Сведения о приостановлении действия лицензии', on_delete=models.DO_NOTHING)
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector']),
            models.Index(fields=['НомЛиц'])
        ]

    def __str__(self):
        return '%s - %s' % (self.ДатаЛиц, self.НаимЛицВидДеят,)


class СвЛицензияCreate:
    def __init__(self, item):
        if item is not None:
            self.НомЛиц = item.get('НомЛиц')
            self.ДатаЛиц = item.get('ДатаЛиц')
            self.ДатаНачЛиц = item.get('ДатаНачЛиц')
            self.ДатаОкончЛиц = item.get('ДатаОкончЛиц')
            if item.find('НаимЛицВидДеят') is not None:
                self.НаимЛицВидДеят = item.find('НаимЛицВидДеят').text
            else:
                self.НаимЛицВидДеят = None
            self.МестоДейстЛиц = item.find('МестоДейстЛиц')
            self.ЛицОргВыдЛиц = item.find('ЛицОргВыдЛиц')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))
            self.СвПриостЛиц = СвПриостЛицCreate(item.find('СвПриостЛиц'))

            self.a = СвЛицензия.objects.create(НомЛиц=self.НомЛиц,
                                               ГРНДата=self.ГРНДата.save(),
                                               НаимЛицВидДеят=self.НаимЛицВидДеят,
                                               ГРНДатаИспр=self.ГРНДатаИспр.save(),
                                               СвПриостЛиц=self.СвПриостЛиц.save())
            self.a.search_vector = vector()
            if self.ДатаЛиц is not None:
                self.a.ДатаЛиц = datetime.strptime(self.ДатаЛиц, '%Y-%m-%d')
            if self.ДатаНачЛиц is not None:
                self.a.ДатаНачЛиц = datetime.strptime(self.ДатаНачЛиц, '%Y-%m-%d')
            if self.ДатаОкончЛиц is not None:
                self.a.ДатаОкончЛиц = datetime.strptime(self.ДатаОкончЛиц, '%Y-%m-%d')

            if self.МестоДейстЛиц is not None:
                self.a.МестоДейстЛиц = self.МестоДейстЛиц.text
            if self.ЛицОргВыдЛиц is not None:
                self.a.ЛицОргВыдЛиц = self.ЛицОргВыдЛиц.text


        else:
            self.a = None

    def save(self):
        if self.a is not None:

            self.a.save()
        return self.a
