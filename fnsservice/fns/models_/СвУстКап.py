from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СведУмУК import СведУмУК, СведУмУКCreate
from .ДробьТип import ДробьТип, ДробьТипCreate


class СвУстКап(models.Model): #4.23
    НаимВидКап = models.CharField(max_length=20, null=True, verbose_name='Наименование вида капитала')
    СумКап = models.FloatField(null=True, verbose_name='Размер в рублях')
    ДоляРубля = models.ForeignKey(ДробьТип, null=True, blank=True,
                                  verbose_name='Доля рубля в капитале', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвУстКап_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)
    СведУмУК = models.ForeignKey(СведУмУК, null=True, blank=True,
                                  verbose_name='Сведения о нахождении хозяйственного общества в процессе уменьшения уставного капитала', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s р.' % (self.НаимВидКап, self.СумКап,)

    class Meta:
        indexes = [
            models.Index(fields=['НаимВидКап', 'СумКап', ])
        ]

class СвУстКапCreate:

    def __init__(self, item):
        if item is not None:
            self.НаимВидКап = item.get('НаимВидКап')
            self.СумКап = item.get('СумКап')
            self.ДоляРубля = ДробьТипCreate(item.find('ДоляРубля'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))
            self.СведУмУК = СведУмУКCreate(item.find('СведУмУК'))

            self.a = СвУстКап.objects.create(НаимВидКап=self.НаимВидКап, СумКап=float(self.СумКап),
                                             ДоляРубля=self.ДоляРубля.save(),
                                             ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save(),
                                             СведУмУК=self.СведУмУК.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
