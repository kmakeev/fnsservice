from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвЮЛЕГРЮЛТип import СвЮЛЕГРЮЛТип, СвЮЛЕГРЮЛТипCreate
from .СвНомТелТип import СвНомТелТип, СвНомТелТипCreate
from .СвРегИнЮЛЕГРЮЛТип import СвРегИнЮЛЕГРЮЛТип, СвРегИнЮЛЕГРЮЛТипCreate
from .СвНедДанУпрОрг import СвНедДанУпрОрг, СвНедДанУпрОргCreate
from .АдрРФЕГРЮЛТип import АдрРФЕГРЮЛТип, АдрРФЕГРЮЛТипCreate
from .СвПредЮЛ import СвПредЮЛ, СвПредЮЛCreate
from .ПредИнЮЛ import ПредИнЮЛ, ПредИнЮЛCreate


class СвУпрОрг(models.Model): #4.27
    ГРНДатаПерв = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ сведений о данном лице', on_delete=models.DO_NOTHING)
    НаимИННЮЛ = models.ForeignKey(СвЮЛЕГРЮЛТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ сведений о данном лице', on_delete=models.DO_NOTHING)
    СвРегИн = models.ForeignKey(СвРегИнЮЛЕГРЮЛТип, null=True, blank=True,
                                verbose_name='Сведения о регистрации в стране происхождения', on_delete=models.DO_NOTHING)
    СвНедДанУпрОрг = models.ManyToManyField(СвНедДанУпрОрг, verbose_name='Сведения о недостоверности данных об управляющей организации')

    СвПредЮЛ = models.ForeignKey(СвПредЮЛ, null=True, blank=True,
                                verbose_name='Сведения о наименовании представительства или филиала в Российской Федерации, через которое иностранное ЮЛ осуществляет полномочия управляющей организации', on_delete=models.DO_NOTHING)
    СвАдрРФ = models.ForeignKey(АдрРФЕГРЮЛТип, null=True, blank=True,
                                verbose_name='Сведения об адресе управляющей организации в Российской Федерации', on_delete=models.DO_NOTHING)
    СвНомТел = models.ForeignKey(СвНомТелТип, null=True, blank=True,
                                verbose_name='Сведения о контактном телефоне', on_delete=models.DO_NOTHING)
    ПредИнЮЛ = models.ForeignKey(ПредИнЮЛ, null=True, blank=True,
                                verbose_name='Сведения об адресе управляющей организации в Российской Федерации', on_delete=models.DO_NOTHING)


    def __str__(self):
        return '%s' % (self.ГРНДатаПерв,)


class СвУпрОргCreate:

    def __init__(self, item):
        if item is not None:
            self.ГРНДатаПерв = ГРНДатаТипCreate(item.find('ГРНДатаПерв'))
            self.НаимИННЮЛ = СвЮЛЕГРЮЛТипCreate(item.find('НаимИННЮЛ'))
            self.СвРегИн = СвРегИнЮЛЕГРЮЛТипCreate(item.find('СвРегИн'))
            self.СвПредЮЛ = СвПредЮЛCreate(item.find('СвПредЮЛ'))
            self.СвАдрРФ = АдрРФЕГРЮЛТипCreate(item.find('СвАдрРФ'))
            self.СвНомТел = СвНомТелТипCreate(item.find('СвНомТел'))
            self.ПредИнЮЛ = ПредИнЮЛCreate(item.find('ПредИнЮЛ'))


            self.a = СвУпрОрг.objects.create(ГРНДатаПерв=self.ГРНДатаПерв.save(),
                                            НаимИННЮЛ=self.НаимИННЮЛ.save(),
                                            СвРегИн=self.СвРегИн.save(),
                                            СвПредЮЛ=self.СвПредЮЛ.save(),
                                            СвАдрРФ=self.СвАдрРФ.save(),
                                            СвНомТел=self.СвНомТел.save(),
                                            ПредИнЮЛ=self.ПредИнЮЛ.save())
            self.СвНедДанУпрОрг = [СвНедДанУпрОргCreate(i) for i in item.findall('СвНедДанУпрОрг')]
            for one_СвНедДанУпрОрг in self.СвНедДанУпрОрг:
                self.a.СвНедДанУпрОрг.add(one_СвНедДанУпрОрг.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a
