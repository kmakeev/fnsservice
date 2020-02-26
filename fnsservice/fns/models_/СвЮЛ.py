from django.db import models
from .СвНаимЮЛ import СвНаимЮЛ, СвНаимЮЛCreate, СвНаимЮЛSerializer
from .СвАдресЮЛ import СвАдресЮЛ, СвАдресЮЛCreate, СвАдресЮЛSerializer
from .СвАдрЭлПочты import СвАдрЭлПочты, СвАдрЭлПочтыCreate
from .СвОбрЮЛ import СвОбрЮЛ, СвОбрЮЛCreate
from .СвРегОрг import СвРегОрг, СвРегОргCreate
from .СвПрекрЮЛ import СвПрекрЮЛ, СвПрекрЮЛCreate, СвПрекрЮЛSerializer
from .СвУчетНО import СвУчетНО, СвУчетНОCreate
from .СвРегПФ import СвРегПФ, СвРегПФCreate
from .СвРегФСС import СвРегФСС, СвРегФССCreate
from .СвУстКап import СвУстКап, СвУстКапCreate
from .СвТипУстав import СвТипУстав, СвТипУставCreate
from .СвУпрОрг import СвУпрОрг, СвУпрОргCreate
from .СведДолжнФЛ import СведДолжнФЛ, СведДолжнФЛCreate
from .СвУчредит import СвУчредит, СвУчредитCreate
from .ДоляУстКапЕГРЮЛТип import ДоляУстКапЕГРЮЛТип, ДоляУстКапЕГРЮЛТипCreate
from .СвДержРеестрАО import СвДержРеестрАО, СвДержРеестрАОCreate
from .СвОКВЭД import СвОКВЭД, СвОКВЭДCreate
from .СвЛицензия import СвЛицензия, СвЛицензияCreate
from .СвПодразд import СвПодразд, СвПодраздCreate
from .СвРеорг import СвРеорг, СвРеоргCreate
from .СвПредш import СвПредш, СвПредшCreate
from .СвКФХПредш import СвКФХПредш, СвКФХПредшCreate
from .СвПреем import СвПреем, СвПреемCreate
from .СвКФХПреем import СвКФХПреем, СвКФХПреемCreate
from .СвЗапЕГРЮЛ import СвЗапЕГРЮЛ, СвЗапЕГРЮЛCreate
from datetime import datetime

from .ГРНДатаТип import ГРНДатаТип, ГРНДатаТипCreate
from .СвРешИсклЮЛ import СвРешИсклЮЛ, СвРешИсклЮЛCreate
from .Св_Статус import Св_Статус, Св_СтатусCreate

from rest_framework import serializers


class СвСтатус(models.Model):  # 4.13
    #СвЮЛ = models.ForeignKey(СвЮЛ, null=True, blank=True,
    #                                  verbose_name='Сведения о состоянии (статусе) юридического лица')

    Св_Статус = models.ForeignKey(Св_Статус, null=True, blank=True,
                                 verbose_name='Сведения о правоспособности (статусе) юридического лица', on_delete=models.DO_NOTHING)
    СвРешИсклЮЛ = models.ForeignKey(СвРешИсклЮЛ, null=True, blank=True,
                                    verbose_name='Сведения о решении о предстоящем исключении недействующего ЮЛ из ЕГРЮЛ и его публикации ', on_delete=models.DO_NOTHING)
    ГРНДата = models.ForeignKey(ГРНДатаТип, null=True, blank=True, related_name='СвСтатус_Дата',
                                verbose_name='ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения', on_delete=models.DO_NOTHING)

    ГРНДатаИспр = models.ForeignKey(ГРНДатаТип, null=True, blank=True,
                                    verbose_name='ГРН и дата внесения в ЕГРЮЛ записи об исправлении технической ошибки в указанных сведениях ', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s' % (self.СвСтатус.__str__,)


class СвСтатусSerializer(serializers.ModelSerializer):

    class Meta:
        model = СвСтатус
        fields = ('ГРНДата',)


class СвЮЛ(models.Model): # 4.4
    СпрОПФ_choises = (
        ('ОКОПФ', 'ОКОПФ'),
        ('КОПФ', 'КОПФ'),
    )
    AddDate = models.DateField(auto_now_add=True, null=False,
                               verbose_name='Дата добавления записи')
    ДатаВып = models.DateField(auto_now=False, auto_now_add=False, null=True, verbose_name='Дата формирования сведений из ЕГРЮЛ в отношении юридического лица')
    ОГРН = models.CharField(max_length=13, verbose_name='Основной государственный регистрационный номер юридического лица')
    ДатаОГРН = models.DateField(auto_now=False, null=True, auto_now_add=False, verbose_name='Дата присвоения ОГРН')
    ИНН = models.CharField(max_length=10, null=True, verbose_name='ИНН юридического лица')
    КПП = models.CharField(max_length=9, null=True, verbose_name='КПП юридического лица')
    СпрОПФ = models.CharField(max_length=5, null=True, choices=СпрОПФ_choises, verbose_name='Наименование классификатора, по которому введены сведения об организационно-правовой форме: ОКОПФ, КОПФ')
    КодОПФ =models.CharField(max_length=5, null=True, verbose_name='Код по выбранному классификатору')
    ПолнНаимОПФ = models.CharField(max_length=255, null=True, verbose_name='Полное наименование организационно-правовой формы')

    СвНаимЮЛ = models.ForeignKey(СвНаимЮЛ, null=True, blank=True, verbose_name='Сведения о наименовании юридического лица', on_delete=models.DO_NOTHING)
    СвАдресЮЛ = models.ForeignKey(СвАдресЮЛ, null=True, blank=True, verbose_name='Сведения об адресе (месте нахождения)', on_delete=models.DO_NOTHING)
    СвАдрЭлПочты = models.ForeignKey(СвАдрЭлПочты, null=True, blank=True,
                                  verbose_name='Сведения об адресе электронной почты юридического лица', on_delete=models.DO_NOTHING)
    СвОбрЮЛ = models.ForeignKey(СвОбрЮЛ, null=True, blank=True,
                                  verbose_name='Сведения о регистрации (образовании) юридического лица', on_delete=models.DO_NOTHING)
    СвРегОрг = models.ForeignKey(СвРегОрг, null=True, blank=True,
                                verbose_name='Сведения о регистрирующем органе по месту нахождения юридического лица', on_delete=models.DO_NOTHING)
    СвСтатус = models.ManyToManyField(СвСтатус, verbose_name='Сведения о состоянии (статусе) юридического лица')

    СвПрекрЮЛ = models.ForeignKey(СвПрекрЮЛ, null=True, verbose_name='Сведения о прекращении юридического лица', on_delete=models.DO_NOTHING)
    СвУчетНО = models.ForeignKey(СвУчетНО, null=True, blank=True,
                                  verbose_name='Сведения об учете в налоговом органе', on_delete=models.DO_NOTHING)
    СвРегПФ = models.ForeignKey(СвРегПФ, null=True, blank=True,
                                  verbose_name='Сведения о регистрации юридического лица в качестве страхователя в территориальном органе Пенсионного фонда Российской Федерации', on_delete=models.DO_NOTHING)
    СвРегФСС = models.ForeignKey(СвРегФСС, null=True, blank=True,
                                  verbose_name='Сведения о регистрации юридического лица в качестве страхователя в исполнительном органе Фонда социального страхования Российской Федерации', on_delete=models.DO_NOTHING)

    СвУстКап = models.ForeignKey(СвУстКап, null=True, blank=True,
                                  verbose_name='Сведения о размере указанного в учредительных документах коммерческой организации уставного капитала (складочного капитала, уставного фонда, паевого фонда)', on_delete=models.DO_NOTHING)
    СвТипУстав = models.ForeignKey(СвТипУстав, null=True, blank=True,
                                 verbose_name='Сведения об использовании юридическим лицом типового устава', on_delete=models.DO_NOTHING)
    СвУпрОрг = models.ManyToManyField(СвУпрОрг, verbose_name='Сведения об учете в налоговом органе')
    СведДолжнФЛ = models.ManyToManyField(СведДолжнФЛ, verbose_name='Сведения о лице, имеющем право без доверенности действовать от имени юридического лица ')
    СвУчредит = models.ForeignKey(СвУчредит, null=True, blank=True,
                                 verbose_name='Сведения об учредителях (участниках) юридического лица', on_delete=models.DO_NOTHING)
    СвСвДоляООО = models.ForeignKey(ДоляУстКапЕГРЮЛТип, null=True, blank=True,
                                  verbose_name='Сведения о доле в уставном капитале общества с ограниченной ответственностью, принадлежащей обществу', on_delete=models.DO_NOTHING)
    СвДержРеестрАО = models.ForeignKey(СвДержРеестрАО, null=True, blank=True,
                                    verbose_name='Сведения о держателе реестра акционеров акционерного общества', on_delete=models.DO_NOTHING)
    СвОКВЭД = models.ForeignKey(СвОКВЭД, null=True, blank=True,
                                       verbose_name='Сведения о видах экономической деятельности по Общероссийскому классификатору видов экономической деятельности', on_delete=models.DO_NOTHING)
    СвЛицензия = models.ManyToManyField(СвЛицензия, verbose_name='Сведения о лицензиях, выданных ЮЛ')
    СвПодразд = models.ForeignKey(СвПодразд, null=True, blank=True,
                                verbose_name='Сведения об обособленных подразделениях юридического лица', on_delete=models.DO_NOTHING)
    СвРеорг = models.ManyToManyField(СвРеорг, verbose_name='Сведения об участии в реорганизации')
    СвПредш = models.ManyToManyField(СвПредш, verbose_name='Сведения о правопредшественнике')
    СвКФХПредш = models.ManyToManyField(СвКФХПредш, verbose_name='Сведения о крестьянском (фермерском) хозяйстве, на базе имущества которого создано юридическое лицо')
    СвПреем = models.ManyToManyField(СвПреем,
                                        verbose_name='Сведения о правопреемнике')
    СвКФХПреем = models.ForeignKey(СвКФХПреем, null=True, blank=True,
                                  verbose_name='Сведения о крестьянском (фермерском) хозяйстве, которые внесены в ЕГРИП в связи с приведением правового статуса крестьянского (фермерского) хозяйства в соответствие с нормами части первой Гражданского кодекса Российской Федерации', on_delete=models.DO_NOTHING)
    СвЗапЕГРЮЛ = models.ManyToManyField(СвЗапЕГРЮЛ,
                                     verbose_name='Сведения о правопреемнике')
    КолЗапЕГРЮЛ = models.IntegerField(null=True, verbose_name='Количество записей в ЕГРЮЛ')

    class Meta:
        indexes = [
            models.Index(fields=['ИНН', 'КПП', 'ОГРН', 'ДатаВып', 'ДатаОГРН'])
        ]

    def __str__(self):
        return 'ОГРН - %s, %s, %s ' % (self.ОГРН, self.СвНаимЮЛ.__str__(), self.СвАдресЮЛ.__str__(), )


class СвСтатусCreate:
    def __init__(self, item):
        if item is not None:
            self.Св_Статус = Св_СтатусCreate(item.find('СвСтатус'))
            self.СвРешИсклЮЛ = СвРешИсклЮЛCreate(item.find('СвРешИсклЮЛ'))
            self.ГРНДата = ГРНДатаТипCreate(item.find('ГРНДата'))
            self.ГРНДатаИспр = ГРНДатаТипCreate(item.find('ГРНДатаИспр'))

            self.a = СвСтатус.objects.create(Св_Статус=self.Св_Статус.save(), СвРешИсклЮЛ=self.СвРешИсклЮЛ.save(),
                                             ГРНДата=self.ГРНДата.save(), ГРНДатаИспр=self.ГРНДатаИспр.save())
        else:
            self.a = None

    def save(self):
        if self.a is not None:
            self.a.save()
        return self.a


class СвЮЛCreate:

    def __init__(self, item):
        self.ДатаВып = item.get('ДатаВып')
        self.ОГРН = item.get('ОГРН')
        self.ДатаОГРН = item.get('ДатаОГРН')
        self.ИНН = item.get('ИНН')
        self.КПП = item.get('КПП')
        self.СпрОПФ = item.get('СпрОПФ')
        self.КодОПФ = item.get('КодОПФ')
        self.ПолнНаимОПФ = item.get('ПолнНаимОПФ')

        self.СвНаимЮЛ = СвНаимЮЛCreate(item.find('СвНаимЮЛ'))
        self.СвАдресЮЛ = СвАдресЮЛCreate(item.find('СвАдресЮЛ'))
        self.СвАдрЭлПочты = СвАдрЭлПочтыCreate(item.find('СвАдрЭлПочты'))
        self.СвОбрЮЛ = СвОбрЮЛCreate(item.find('СвОбрЮЛ'))
        self.СвРегОрг = СвРегОргCreate(item.find('СвРегОрг'))
        # self.СвСтатус = СвСтатусCreate(item.find('СвСтатус'))
        self.СвПрекрЮЛ = СвПрекрЮЛCreate(item.find('СвПрекрЮЛ'))
        self.СвУчетНО = СвУчетНОCreate(item.find('СвУчетНО'))
        self.СвРегПФ = СвРегПФCreate(item.find('СвРегПФ'))
        self.СвРегФСС = СвРегФССCreate(item.find('СвРегФСС'))
        self.СвУстКап = СвУстКапCreate(item.find('СвУстКап'))
        self.СвТипУстав = СвТипУставCreate(item.find('СвТипУстав'))
        self.СвУчредит = СвУчредитCreate(item.find('СвУчредит'))
        self.СвСвДоляООО = ДоляУстКапЕГРЮЛТипCreate(item.find('СвДоляООО'))
        self.СвДержРеестрАО = СвДержРеестрАОCreate(item.find('СвДержРеестрАО'))
        self.СвОКВЭД = СвОКВЭДCreate(item.find('СвОКВЭД'))
        self.СвПодразд = СвПодраздCreate(item.find('СвПодразд'))
        self.СвКФХПреем = СвКФХПреемCreate(item.find('СвКФХПреем'))
        self.СвЗапЕГРЮЛ = [СвЗапЕГРЮЛCreate(i) for i in item.findall('СвЗапЕГРЮЛ')]
        self.КолЗапЕГРЮЛ = len(self.СвЗапЕГРЮЛ)
        self.a = СвЮЛ.objects.create(ДатаВып=datetime.strptime(self.ДатаВып, '%Y-%m-%d'),
                                     ОГРН=self.ОГРН,
                                     ДатаОГРН=datetime.strptime(self.ДатаОГРН, '%Y-%m-%d'),
                                     ИНН=self.ИНН,
                                     КПП=self.КПП,
                                     СпрОПФ=self.СпрОПФ,
                                     КодОПФ=self.КодОПФ,
                                     ПолнНаимОПФ=self.ПолнНаимОПФ,
                                     СвНаимЮЛ=self.СвНаимЮЛ.save(),
                                     СвАдресЮЛ=self.СвАдресЮЛ.save(),
                                     СвАдрЭлПочты=self.СвАдрЭлПочты.save(),
                                     СвОбрЮЛ=self.СвОбрЮЛ.save(),
                                     СвРегОрг=self.СвРегОрг.save(),
                                     СвПрекрЮЛ=self.СвПрекрЮЛ.save(),
                                     СвУчетНО=self.СвУчетНО.save(),
                                     СвРегПФ=self.СвРегПФ.save(),
                                     СвРегФСС=self.СвРегФСС.save(),
                                     СвУстКап=self.СвУстКап.save(),
                                     СвТипУстав=self.СвТипУстав.save(),
                                     СвУчредит=self.СвУчредит.save(),
                                     СвСвДоляООО=self.СвСвДоляООО.save(),
                                     СвДержРеестрАО=self.СвДержРеестрАО.save(),
                                     СвОКВЭД=self.СвОКВЭД.save(),
                                     СвПодразд=self.СвПодразд.save(),
                                     СвКФХПреем=self.СвКФХПреем.save(),
                                     КолЗапЕГРЮЛ=self.КолЗапЕГРЮЛ)

        self.СвУпрОрг = [СвУпрОргCreate(i) for i in item.findall('СвУпрОрг')]
        for one_СвУпрОрг in self.СвУпрОрг:
            self.a.СвУпрОрг.add(one_СвУпрОрг.save())
        self.СвСтатус = [СвСтатусCreate(i) for i in item.findall('СвСтатус')]
        for one_СвСтатус in self.СвСтатус:
            self.a.СвСтатус.add(one_СвСтатус.save())
        self.СведДолжнФЛ = [СведДолжнФЛCreate(i) for i in item.findall('СведДолжнФЛ')]
        for one_СведДолжнФЛ in self.СведДолжнФЛ:
            self.a.СведДолжнФЛ.add(one_СведДолжнФЛ.save())
        self.СвЛицензия = [СвЛицензияCreate(i) for i in item.findall('СвЛицензия')]
        for one_СвЛицензия in self.СвЛицензия:
            self.a.СвЛицензия.add(one_СвЛицензия.save())
        self.СвРеорг = [СвРеоргCreate(i) for i in item.findall('СвРеорг')]
        for one_СвРеорг in self.СвРеорг:
            self.a.СвРеорг.add(one_СвРеорг.save())
        self.СвПредш = [СвПредшCreate(i) for i in item.findall('СвПредш')]
        for one_СвПредш in self.СвПредш:
            self.a.СвПредш.add(one_СвПредш.save())
        self.СвКФХПредш = [СвКФХПредшCreate(i) for i in item.findall('СвКФХПредш')]
        for one_СвКФХПредш in self.СвКФХПредш:
            self.a.СвКФХПредш.add(one_СвКФХПредш.save())
        self.СвПреем = [СвПреемCreate(i) for i in item.findall('СвПреем')]
        for one_СвПреем in self.СвПреем:
            self.a.СвПреем.add(one_СвПреем.save())
        # self.СвЗапЕГРЮЛ = [СвЗапЕГРЮЛCreate(i) for i in item.findall('СвЗапЕГРЮЛ')]
        for one_СвЗапЕГРЮЛ in self.СвЗапЕГРЮЛ:
            self.a.СвЗапЕГРЮЛ.add(one_СвЗапЕГРЮЛ.save())

    def save(self):
        self.a.save()
        return self.a


class СвЮЛSerializer(serializers.ModelSerializer):

    СвНаимЮЛ = СвНаимЮЛSerializer(many=False)
    СвАдресЮЛ = СвАдресЮЛSerializer(many=False)
    СвПрекрЮЛ = СвПрекрЮЛSerializer(many=False)
    СвСтатус = СвСтатусSerializer(many=True)

    class Meta:
        model = СвЮЛ
        fields = ('ДатаВып', 'ОГРН', 'ДатаОГРН', 'ИНН', 'КПП', 'СвНаимЮЛ', 'СвАдресЮЛ', 'СвПрекрЮЛ', 'СвСтатус')
