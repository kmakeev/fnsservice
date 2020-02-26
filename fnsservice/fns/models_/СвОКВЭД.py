from django.db import models
from .СвОКВЭДТип import СвОКВЭДТип, СвОКВЭДТипCreate


class СвОКВЭД(models.Model): #4.51

    СвОКВЭДОсн = models.ForeignKey(СвОКВЭДТип, null=True, blank=True, related_name='СвОКВЭДТип_First', verbose_name='Сведения об основном виде деятельности', on_delete=models.DO_NOTHING)
    СвОКВЭДДоп = models.ManyToManyField(СвОКВЭДТип, verbose_name='Сведения о дополнительном виде деятельности')

    def __str__(self):
        return '%s' % (self.СвОКВЭДОсн,)


class СвОКВЭДCreate:

    def __init__(self, item):
        if item is not None:

            self.СвОКВЭДОсн = СвОКВЭДТипCreate(item.find('ГСвОКВЭДОсн'))
            self.a = СвОКВЭД.objects.create(СвОКВЭДОсн=self.СвОКВЭДОсн.save())

            self.СвОКВЭДДоп = [СвОКВЭДТипCreate(i) for i in item.findall('СвОКВЭДДоп')]
            for one_СвОКВЭДДоп in self.СвОКВЭДДоп:
                self.a.СвОКВЭДДоп.add(one_СвОКВЭДДоп.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
