from django.db import models
from .СвФЛЕГРЮЛТип import СвФЛЕГРЮЛТип, СвФЛЕГРЮЛТипCreate


class СвКФХПреем(models.Model): #4.63
    ОГРНИП = models.CharField(max_length=15, null=True, blank=True, verbose_name='ОГРНИП крестьянского (фермерского) хозяйства')

    СвФЛ = models.ForeignKey(СвФЛЕГРЮЛТип, null=True, blank=True,
                                verbose_name='Сведения о ФИО и (при наличии) ИНН главы КФХ', on_delete=models.DO_NOTHING)


    def __str__(self):
        return '%s - %s' % (self.ОГРН, self.СвФЛ,)


class СвКФХПреемCreate:

    def __init__(self, item):
        if item is not None:
            self.ОГРНИП = item.get('ОГРНИП')
            self.СвФЛ = СвФЛЕГРЮЛТипCreate(item.find('СвФЛ'))

            self.a = СвКФХПреем.objects.create(ОГРНИП=self.ОГРНИП,
                                               СвФЛ=self.СвФЛ.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
