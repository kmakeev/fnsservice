from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .РегионТип import РегионТип, РегионТипCreate
from .РайонТип import РайонТип, РайонТипCreate
from .ГородТип import ГородТип, ГородТипCreate
from .НаселПунктТип import НаселПунктТип, НаселПунктТипCreate


class СвРешИзмМН(models.Model):  #4.8
    ТекстРешИзмМН = models.CharField(max_length=500, null=True, verbose_name='Текст, выводимый в выписке в строке с наименованием «Дополнительные сведения»')
    Регион = models.ForeignKey(РегионТип, null=True, blank=True, verbose_name='Субъект Российской Федерации', on_delete=models.DO_NOTHING)
    Район = models.ForeignKey(РайонТип, null=True, blank=True, verbose_name='Район (улус и т.п.)', on_delete=models.DO_NOTHING)
    Город = models.ForeignKey(ГородТип, null=True, blank=True, verbose_name='Город (волость и т.п.)', on_delete=models.DO_NOTHING)
    НаселПункт = models.ForeignKey(НаселПунктТип, null=True, blank=True, verbose_name='Населенный пункт (село и т.п.)', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвРешИзмМН_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s ' % (self.ТекстРешИзмМН,)


class СвРешИзмМНCreate:

    def __init__(self, item):
        if item is not None:
            self.ТекстРешИзмМН = item.get('ТекстРешИзмМН')
            self.Регион = РегионТипCreate(item.find('Регион'))
            self.Район = РайонТипCreate(item.find('Район'))
            self.Город = ГородТипCreate(item.find('Город'))
            self.НаселПункт = НаселПунктТипCreate(item.find('НаселПункт'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвРешИзмМН.objects.create(ТекстРешИзмМН=self.ТекстРешИзмМН, Регион=self.Регион.save(),
                                               Район=self.Район.save(), Город=self.Город.save(), НаселПункт=self.НаселПункт.save(),
                                               ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
