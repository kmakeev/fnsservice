from django.db import models
from . ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate


class СвАдрЭлПочты(models.Model): #4.9
    E_mail = models.CharField(max_length=45, null=True, verbose_name='Адрес электронной почты')
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвАдрЭлПочты_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                    verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s' % (self.E_mail,)


class СвАдрЭлПочтыCreate:
    def __init__(self, mail):
        if mail is not None:
            self.E_mail = mail.get('E-mail')
            self.ГРНДата = ГРНДатаТипCreate(mail.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(mail.find('ГРНДатаИспр'))
            self.a = СвАдрЭлПочты.objects.create(E_mail=self.E_mail, ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
