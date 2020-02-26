from django.db import models
from .СвФилиал import СвФилиал, СвФилиалCreate
from .СвПредстав import СвПредстав, СвПредставCreate


class СвПодразд(models.Model): #4.54

    СвФилиал = models.ManyToManyField(СвФилиал, verbose_name='Сведения о филиалах юридического лица')
    СвПр = models.ManyToManyField(СвПредстав, verbose_name='Сведения о представительствах юридического лица')


class СвПодраздCreate:

    def __init__(self, item):
        if item is not None:

            self.a = СвПодразд.objects.create()

            self.СвФилиал = [СвФилиалCreate(i) for i in item.findall('СвФилиал')]
            for one_СвФилиал in self.СвФилиал:
                self.a.СвФилиал.add(one_СвФилиал.save())
            self.СвПредстав = [СвПредставCreate(i) for i in item.findall('СвПредстав')]
            for one_СвПредстав in self.СвПредстав:
                self.a.СвПр.add(one_СвПредстав.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
