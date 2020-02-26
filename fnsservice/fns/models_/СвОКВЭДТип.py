from django.db import models
from . ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVector, SearchVectorField

def vector():
    return SearchVector('НаимОКВЭД', config='russian')

class СвОКВЭДТип(models.Model): #4.101
    КодОКВЭД = models.CharField(max_length=8, null=True, blank=True,
                              verbose_name='Код по Общероссийскому классификатору видов экономической деятельности')
    НаимОКВЭД = models.CharField(max_length=1000, null=True, blank=True,
                                verbose_name='Наименование вида деятельности по Общероссийскому классификатору видов экономической деятельности')
    ПрВерсОКВЭД = models.CharField(max_length=4, null=True, blank=True,
                                verbose_name='Код по Общероссийскому классификатору видов экономической деятельности')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвОКВЭДТип_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector']),
            models.Index(fields=['КодОКВЭД', 'ПрВерсОКВЭД'])
        ]

    def __str__(self):
        return '%s - %s' % (self.ОКВЭД, self.НаимОКВЭД,)


class СвОКВЭДТипCreate:
    def __init__(self, item):
        if item is not None:
            self.КодОКВЭД = item.get('КодОКВЭД')
            self.НаимОКВЭД = item.get('НаимОКВЭД')
            self.ПрВерсОКВЭД = item.get('ПрВерсОКВЭД')
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            try:
                b = СвОКВЭДТип.objects.get(КодОКВЭД=self.КодОКВЭД, ПрВерсОКВЭД=self.ПрВерсОКВЭД)
                self.a = b
            except:
                self.a = СвОКВЭДТип.objects.create(КодОКВЭД=self.КодОКВЭД,
                                                   НаимОКВЭД=self.НаимОКВЭД,
                                                   ПрВерсОКВЭД=self.ПрВерсОКВЭД,
                                                   ГРНДата=self.ГРНДата.save(),
                                                   ГРНДатаИспр=self.ГРНДатаИспр.save())
                self.a.search_vector = vector()
                self.a.save()
        else:
            self.a = None

    def save(self):
        #if self.a is not None:
        #    self.a.save()
        return self.a
