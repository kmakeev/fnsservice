from django.db import models
from .ВидЗаяв import ВидЗаяв, ВидЗаявCreate
from .Св_ЮЛ import Св_ЮЛ, Св_ЮЛCreate
from .Св_УпрОрг import Св_УпрОрг, Св_УпрОргCreate
from .СвФЛ import СвФЛ, СвФЛCreate


class СвЗаявФЛ(models.Model): #4.67

    ВидЗаяв = models.ForeignKey(ВидЗаяв, null=True, blank=True,
                             verbose_name='Заявитель', on_delete=models.DO_NOTHING)
    СвЮЛ = models.ForeignKey(Св_ЮЛ, null=True, blank=True,
                                 verbose_name='Сведения о юридическом лице, от имени которого действует заявитель', on_delete=models.DO_NOTHING)

    СвУпрОрг = models.ForeignKey(Св_УпрОрг, null=True, blank=True,
                                verbose_name='Сведения об управляющей компании', on_delete=models.DO_NOTHING)
    СвФЛ = models.ForeignKey(СвФЛ, null=True, blank=True,
                             verbose_name='ССведения о ФЛ - заявителе', on_delete=models.DO_NOTHING)


class СвЗаявФЛCreate:

    def __init__(self, item):
        if item is not None:
            self.ВидЗаяв = ВидЗаявCreate(item.find('ВидЗаяв'))
            self.СвЮЛ = Св_ЮЛCreate(item.find('СвЮЛ'))
            self.СвУпрОрг = Св_УпрОргCreate(item.find('СвУпрОрг'))
            self.СвФЛ = СвФЛCreate(item.find('СвФЛ'))

            self.a = СвЗаявФЛ.objects.create(ВидЗаяв=self.ВидЗаяв.save(),
                                             СвЮЛ=self.СвЮЛ.save(),
                                             СвУпрОрг=self.СвУпрОрг.save(),
                                             СвФЛ=self.СвФЛ.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
