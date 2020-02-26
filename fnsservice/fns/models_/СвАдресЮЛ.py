from django.db import models
from .АдрРФЕГРЮЛТип import АдрРФЕГРЮЛТип, АдрРФЕГРЮЛТипCreate, АдрРФЕГРЮЛТипSerializer
# from .СвНедАдресЮЛ import СвНедАдресЮЛCreate
from .СвРешИзмМН import СвРешИзмМН, СвРешИзмМНCreate
from .РешСудТип import РешСудТип, РешСудТипCreate
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from rest_framework import serializers
from rest_framework import serializers


class СвНедАдресЮЛ(models.Model): #4.7
    ПризнНедАдресЮЛ_choises = (
        ('2', 'признак недостоверности, внесенный в ЕГРЮЛ по результатам проверки достоверности содержащихся в ЕГРЮЛ сведений о юридическом лице (если сведения о недостоверности сведений об адресе внесены на основании записи с кодом СПВЗ 17023)'),
        ('3', 'признак недостоверности, внесенный в ЕГРЮЛ на основании решения суда (если сведения о недостоверности сведений об адресе внесены на основании записи с кодом СПВЗ 16006)'),
    )

    # СвАдресЮЛ = models.ForeignKey(СвАдресЮЛ, null=True, blank=True, verbose_name='Сведения о решении суда, на основании которого адрес признан недостоверным')
    ПризнНедАдресЮЛ = models.CharField(max_length=1, null=True, choices=ПризнНедАдресЮЛ_choises,
                              verbose_name='Признак недостоверности адреса ')
    ТекстНедАдресЮЛ = models.CharField(max_length=500, null=True, blank=True,
                                  verbose_name='Текст о недостоверности сведений, выводимый в выписке в строке с наименованием «Дополнительные сведения»')
    РешСудНедАдр = models.ForeignKey(РешСудТип, null=True, blank=True, verbose_name='Сведения о решении суда, на основании которого адрес признан недостоверным', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвНедАдресЮЛ_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                    verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return ' %s - от %s' % (self.ПризнНедАдресЮЛ, self.ТекстНедАдресЮЛ, )


class СвАдресЮЛ(models.Model): #4.6
    АдресРФ = models.ForeignKey(АдрРФЕГРЮЛТип, null=True, blank=True, verbose_name='Адрес (место нахождения) юридического лица', on_delete=models.DO_NOTHING)
    СвНедАдресЮЛ = models.ManyToManyField(СвНедАдресЮЛ, verbose_name='Сведения о недостоверности адреса')
    СвРешИзмМН = models.ForeignKey(СвРешИзмМН, null=True, blank=True, verbose_name='Сведения о принятии юридическим лицом решения об изменении места нахождения', on_delete=models.DO_NOTHING)

    # def __str__(self):
    #    return self.АдресРФ.__str__()


class СвАдресЮЛSerializer(serializers.ModelSerializer):

    #АдресРФ = serializers.StringRelatedField(many=False)
    АдресРФ = АдрРФЕГРЮЛТипSerializer(many=False)

    class Meta:
        model = СвАдресЮЛ
        fields = ('АдресРФ',)


class СвНедАдресЮЛCreate:

    def __init__(self, item):
        if item is not None:
            self.ПризнНедАдресЮЛ = item.get('ПризнНедАдресЮЛ')
            self.ТекстНедАдресЮЛ = item.get('ТекстНедАдресЮЛ')
            self.РешСудНедАдр = РешСудТипCreate(item.find('РешСудНедАдр'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))
            self.a = СвНедАдресЮЛ.objects.create(ПризнНедАдресЮЛ=self.ПризнНедАдресЮЛ, ТекстНедАдресЮЛ=self.ТекстНедАдресЮЛ,
                                                 РешСудНедАдр=self.РешСудНедАдр.save(), ГРНДата=self.ГРНДата.save(),
                                                 ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a


class СвАдресЮЛCreate:

    def __init__(self, item):
        if item is not None:
            self.АдресРФ = АдрРФЕГРЮЛТипCreate(item.find('АдресРФ'))

            #self.СвНедАдресЮЛ = СвНедАдресЮЛCreate(item.find('СвНедАдресЮЛ'))
            self.СвРешИзмМН = СвРешИзмМНCreate(item.find('СвРешИзмМН'))
            self.a = СвАдресЮЛ.objects.create(АдресРФ=self.АдресРФ.save(),
                                              #СвНедАдресЮЛ=self.СвНедАдресЮЛ.save(),
                                              СвРешИзмМН=self.СвРешИзмМН.save())
            for i in item.findall('СвНедАдресЮЛ'):
                self.a.СвНедАдресЮЛ.add(СвНедАдресЮЛCreate(i).save())

        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a


