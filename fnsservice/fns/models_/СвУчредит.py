from django.db import models
from .УчрЮЛРос import УчрЮЛРос, УчрЮЛРосCreate
from .УчрЮЛИн import УчрЮЛИн, УчрЮЛИнCreate
from .УчрФЛ import УчрФЛ, УчрФЛCreate
from .УчрРФСубМО import УчрРФСубМО, УчрРФСубМОCreate
from .УчрПИФ import УчрПИФ, УчрПИФCreate


class СвУчредит(models.Model): #4.35

    УчрЮЛРос = models.ManyToManyField(УчрЮЛРос, verbose_name='Сведения об учредителе (участнике) - российском юридическом лице')
    УчрЮЛИн = models.ManyToManyField(УчрЮЛИн, verbose_name='Сведения об учредителе (участнике) - иностранном юридическом лице')
    УчрФЛ = models.ManyToManyField(УчрФЛ, verbose_name='Сведения об учредителе (участнике) - физическом лице')
    УчрРФСМО = models.ManyToManyField(УчрРФСубМО,
                                        verbose_name='Сведения об учредителе (участнике) - Российской Федерации, субъекте Российской Федерации, муниципальном образовании')
    УчрПИФ = models.ManyToManyField(УчрПИФ,
                                    verbose_name='Сведения о паевом инвестиционном фонде, в состав имущества которого включена доля в уставном капитале ')




    def __str__(self):
        return '%s' % (self.ГРНДатаПерв,)


class СвУчредитCreate:

    def __init__(self, item):
        if item is not None:
            self.a = СвУчредит.objects.create()

            self.УчрЮЛРос = [УчрЮЛРосCreate(i) for i in item.findall('УчрЮЛРос')]
            for one_УчрЮЛРос in self.УчрЮЛРос:
                self.a.УчрЮЛРос.add(one_УчрЮЛРос.save())

            self.УчрЮЛИн = [УчрЮЛИнCreate(i) for i in item.findall('УчрЮЛИн')]
            for one_УчрЮЛИн in self.УчрЮЛИн:
                self.a.УчрЮЛИн.add(one_УчрЮЛИн.save())

            self.УчрФЛ = [УчрФЛCreate(i) for i in item.findall('УчрФЛ')]
            for one_УчрФЛ in self.УчрФЛ:
                self.a.УчрФЛ.add(one_УчрФЛ.save())

            self.УчрРФСубМО = [УчрРФСубМОCreate(i) for i in item.findall('УчрРФСубМО')]
            for one_УчрРФСубМО in self.УчрРФСубМО:
                self.a.УчрРФСМО.add(one_УчрРФСубМО.save())

            self.УчрПИФ = [УчрПИФCreate(i) for i in item.findall('УчрПИФ')]
            for one_УчрПИФ in self.УчрПИФ:
                self.a.УчрПИФ.add(one_УчрПИФ.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a

