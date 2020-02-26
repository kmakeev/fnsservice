from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .Св_Статус import Св_Статус, Св_СтатусCreate
from .СвРеоргЮЛ import СвРеоргЮЛ, СвРеоргЮЛCreate


class СвРеорг(models.Model): #4.57
    СвСтатус = models.ForeignKey(Св_Статус, null=True, blank=True,
                               verbose_name='Сведения о форме реорганизации (статусе) юридического лица', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвРеорг_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей сведения о начале реорганизации', on_delete=models.DO_NOTHING)

    ГРНДатаИзмСост = models.ManyToManyField(ГРНДатаТип,
                                        verbose_name='ГРН и дата внесения записи, которой в ЕГРЮЛ внесены сведения об изменении состава участвующих в реорганизации юридических лиц ')

    СвРеоргЮЛ = models.ManyToManyField(СвРеоргЮЛ,
                               verbose_name='Сведения о юридических лицах, участвующих в реорганизации')


class СвРеоргCreate:

    def __init__(self, item):
        if item is not None:

            self.СвСтатус = Св_СтатусCreate(item.find('СвСтатус'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))

            self.a = СвРеорг.objects.create(ГРНДата=self.ГРНДата.save(),
                                               СвСтатус=self.СвСтатус.save())
            self.ГРНДатаИзмСост = [ГРНДатаТипCreate(i) for i in item.findall('ГРНДатаИзмСостРеоргЮЛ')]
            for one_ГРНДатаИзмСост in self.ГРНДатаИзмСост:
                self.a.ГРНДатаИзмСост.add(one_ГРНДатаИзмСост.save())
            self.СвРеоргЮЛ = [СвРеоргЮЛCreate(i) for i in item.findall('СвРеоргЮЛ')]
            for one_СвРеоргЮЛ in self.СвРеоргЮЛ:
                self.a.СвРеоргЮЛ.add(one_СвРеоргЮЛ.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
