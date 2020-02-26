from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVector, SearchVectorField

def vector():
    return SearchVector('Фамилия', 'Имя', 'Отчество', config='russian')

class СвФЛЕГРЮЛТип(models.Model): # 4.106
    Фамилия = models.CharField(max_length=60, null=True, blank=True,
                              verbose_name='Фамилия')
    Имя = models.CharField(max_length=60, null=True, blank=True,
                               verbose_name='Имя')
    Отчество = models.CharField(max_length=60, null=True, blank=True,
                           verbose_name='Отчество')
    ИННФЛ = models.CharField(max_length=60, null=True, blank=True,
                                verbose_name='ИНН ФЛ')

    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвФЛЕГРЮЛТип_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector']),
            models.Index(fields=['ИННФЛ', 'Фамилия', 'Имя', 'Отчество'])
        ]

    #def __str__(self):
    #    return '%s - %s %s %s ' % (self.ИННФЛ, self.Фамилия, self.Имя, self.Отчество,)


class СвФЛЕГРЮЛТипCreate:

    def __init__(self, item):
        if item is not None:
            self.Фамилия = item.get('Фамилия')
            self.Имя = item.get('Имя')
            self.Отчество = item.get('Отчество')
            self.ИННФЛ = item.get('ИННФЛ')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            try:
                b = СвФЛЕГРЮЛТип.objects.get(Фамилия=self.Фамилия, Имя=self.Имя, Отчество=self.Отчество, ИННФЛ=self.ИННФЛ)
                self.a = b
                # print('СвФЛЕГРЮЛТип is exist', self.ИННФЛ)
            except:
                self.a = СвФЛЕГРЮЛТип.objects.create(Фамилия=self.Фамилия, Имя=self.Имя, Отчество=self.Отчество, ИННФЛ=self.ИННФЛ,
                                                  ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
                self.a.search_vector = vector()
                self.a.save()

        else:
            self.a = None

    def save(self):
        #if self.a is not None:
        #    self.a.save()
        return self.a

