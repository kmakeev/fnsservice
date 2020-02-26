from django.db import models
from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .РегионТип import РегионТип, РегионТипCreate
from .ГородТип import ГородТип, ГородТипCreate
from .УлицаТип import УлицаТип, УлицаТипCreate
from .РайонТип import РайонТип, РайонТипCreate
from .НаселПунктТип import НаселПунктТип, НаселПунктТипCreate
from rest_framework import serializers


class АдрРФЕГРЮЛТип(models.Model): #4.82
    Индекс = models.CharField(max_length=6, null=True, blank=True,
                                  verbose_name='Индекс')
    КодРегион = models.CharField(max_length=2, null=True, blank=True,
                              verbose_name='Код субъекта Российской Федерации')
    КодАдрКладр = models.CharField(max_length=23, null=True, blank=True,
                              verbose_name='Код адреса по КЛАДР')
    Дом = models.CharField(max_length=50, null=True, blank=True,
                              verbose_name='Дом (владение и т.п.)')
    Корпус = models.CharField(max_length=50, null=True, blank=True,
                           verbose_name='Корпус (строение и т.п.)')
    Кварт = models.CharField(max_length=50, null=True, blank=True,
                           verbose_name='Квартира (офис и т.п.)')
    Регион = models.ForeignKey(РегионТип, null=True, blank=True,
                                verbose_name='Субъект Российской Федерации', on_delete=models.DO_NOTHING)
    Район = models.ForeignKey(РайонТип, null=True, blank=True,
                               verbose_name='Район (улус и т.п.)', on_delete=models.DO_NOTHING)
    Город = models.ForeignKey(ГородТип, null=True, blank=True,
                              verbose_name='Город (волость и т.п.)', on_delete=models.DO_NOTHING)
    НаселПункт = models.ForeignKey(НаселПунктТип, null=True, blank=True,
                                   verbose_name='Населенный пункт (село и т.п.)', on_delete=models.DO_NOTHING)
    Улица = models.ForeignKey(УлицаТип, null=True, blank=True,
                              verbose_name='Улица (проспект, переулок и т.п.)', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='АдрРФЕГРЮЛТип_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)
    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    class Meta:
        indexes = [
            models.Index(fields=['Индекс', 'КодРегион', 'КодАдрКладр', ])
        ]

    def __str__(self):

        """
        return '%s, %s %s, %s %s, %s %s, %s %s, %s, %s, %s' % (self.Индекс, self.Регион.ТипРегион, self.Регион.НаимРегион,
                                                               self.Район.ТипРайон, self.Район.НаимРайон,
                                                               self.Город.ТипГород, self.Город.НаимГород,
                                                               self.Улица.ТипУлица, self.Улица.НаимУлица, self.Дом,
                                                               self.Корпус, self.Кварт)
        :return:
        """
        Индекс = self.Индекс
        ТипРег = self.Регион.ТипРегион
        НаимРегион = self.Регион.НаимРегион
        ТипРайон = str('' if self.Район is None else self.Район.ТипРайон)
        return '%s, %s %s' % (Индекс, ТипРег, НаимРегион)


class АдрРФЕГРЮЛТипCreate:

    def __init__(self, item):
        if item is not None:
            self.Индекс = item.get('Индекс')
            self.КодРегион = item.get('КодРегион')
            self.КодАдрКладр = item.get('КодАдрКладр')
            self.Дом = item.get('Дом')
            self.Корпус = item.get('Корпус')
            self.Кварт = item.get('Кварт')
            self.Регион = РегионТипCreate(item.find('Регион'))
            self.Район = РайонТипCreate(item.find('Район'))
            self.Город = ГородТипCreate(item.find('Город'))
            self.НаселПункт = НаселПунктТипCreate(item.find('НаселПункт'))
            self.Улица = УлицаТипCreate(item.find('Улица'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = АдрРФЕГРЮЛТип.objects.create(Индекс=self.Индекс, КодРегион=self.КодРегион, КодАдрКладр=self.КодАдрКладр,
                                                  Дом=self.Дом, Корпус=self.Корпус, Кварт=self.Кварт,
                                                  Регион=self.Регион.save(), Район=self.Район.save(),
                                                  Город=self.Город.save(), НаселПункт=self.НаселПункт.save(), Улица=self.Улица.save(),
                                                  ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a

class АдрРФЕГРЮЛТипSerializer(serializers.ModelSerializer):

    Регион = serializers.StringRelatedField(many=False)
    Район = serializers.StringRelatedField(many=False)
    Город = serializers.StringRelatedField(many=False)
    НаселПункт = serializers.StringRelatedField(many=False)
    Улица = serializers.StringRelatedField(many=False)

    class Meta:
        model = АдрРФЕГРЮЛТип
        fields = ('Индекс', 'КодРегион', 'Регион', 'Район', 'Город', 'НаселПункт', 'Улица', 'Дом', 'Корпус', 'Кварт', 'КодАдрКладр', )