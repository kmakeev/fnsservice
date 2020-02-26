from django.db import models


class Св_ЮЛ(models.Model): #4.69
    ОГРН = models.CharField(max_length=13, null=True,
                            verbose_name='Основной государственный регистрационный номер юридического лица')
    ИНН = models.CharField(max_length=10, null=True, verbose_name='ИНН юридического лица')
    НаимЮЛПолн = models.CharField(max_length=1000, null=True,
                                  verbose_name='Полное наименование юридического лица на русском языке')


    def __str__(self):
        return '%s - %s ' % (self.ОГРН, self.НаимЮЛПолн,)


class Св_ЮЛCreate:

    def __init__(self, item):
        if item is not None:
            self.ОГРН = item.get('ОГРН')
            self.ИНН = item.get('ИНН')
            self.НаимЮЛПолн = item.get('НаимЮЛПолн')

            self.a = Св_ЮЛ.objects.create(ОГРН=self.ОГРН, ИНН=self.ИНН, НаимЮЛПолн=self.НаимЮЛПолн)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
