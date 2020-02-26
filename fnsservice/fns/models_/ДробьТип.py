from django.db import models


class ДробьТип(models.Model): #4.87
    Числит = models.CharField(max_length=15, null=True, blank=True, verbose_name='Числит')
    Знаменат = models.CharField(max_length=15, null=True, blank=True, verbose_name='Знаменат')

    def __str__(self):
        return '%s/%s' % (self.Числит, self.Знаменат,)


class ДробьТипCreate:

    def __init__(self, item):
        if item is not None:
            self.Числит = item.get('Числит')
            self.Знаменат = item.get('Знаменат')
            self.a = ДробьТип.objects.create(Числит=self.Числит, Знаменат=self.Знаменат)

        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
