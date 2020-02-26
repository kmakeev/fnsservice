from django.db import models


class ФИОТип(models.Model):
    Фамилия = models.CharField(max_length=60, blank=True, null=True, verbose_name='Фамилия')
    Имя = models.CharField(max_length=60, blank=True, null=True, verbose_name='Имя')
    Отчество = models.CharField(max_length=60, blank=True, null=True, verbose_name='Отчество')

    def __str__(self):
        return '%s %s %s' % (self.Фамилия, self.Имя, self.Отчество)


class ФИОТипCreate:
    def __init__(self, fio):

        if fio is not None:
            self.Фамилия = fio.get('Фамилия')
            self.Имя = fio.get('Имя')
            self.Отчество = fio.get('Отчество')

            self.a = ФИОТип.objects.create(Фамилия=self.Фамилия, Имя=self.Имя, Отчество=self.Отчество)
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
