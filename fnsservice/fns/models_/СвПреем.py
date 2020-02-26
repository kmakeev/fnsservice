from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвЮЛсложнРеорг import СвЮЛсложнРеорг, СвЮЛсложнРеоргCreate


class СвПреем(models.Model): #4.63
    ОГРН = models.CharField(max_length=13, null=True, blank=True, verbose_name='Основной государственный регистрационный номер юридического лица')
    ИНН = models.CharField(max_length=10, null=True, blank=True,
                            verbose_name='ИНН юридического лица')
    НаимЮЛПолн = models.CharField(max_length=1000, verbose_name='Полное наименование юридического лица')
    СвЮЛсложнРеорг = models.ForeignKey(СвЮЛсложнРеорг, null=True, blank=True,
                                verbose_name='Сведения о ЮЛ, путем реорганизации которого был создан правопредшественник при реорганизации в форме выделения или разделения с одновременным присоединением или слиянием', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвПреем_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                            verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.ОГРН, self.НаимЮЛПолн,)


class СвПреемCreate:

    def __init__(self, item):
        if item is not None:
            self.ОГРН = item.get('ОГРН')
            self.ИНН = item.get('ИНН')
            self.НаимЮЛПолн = item.get('НаимЮЛПолн')
            self.СвЮЛсложнРеорг = СвЮЛсложнРеоргCreate(item.find('СвЮЛсложнРеорг'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвПреем.objects.create(ОГРН=self.ОГРН, ИНН=self.ИНН, НаимЮЛПолн=self.НаимЮЛПолн,
                                            СвЮЛсложнРеорг=self.СвЮЛсложнРеорг.save(), ГРНДата=self.ГРНДата.save(),
                                            ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a