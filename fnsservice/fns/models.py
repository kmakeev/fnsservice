import xml.etree.cElementTree as ET
from django.db.models import F
from django.db import models
from .models_.ИдОтпр import ИдОтпр, ИдОтпрCreate
from .models_.СвЮЛ import СвЮЛ, СвЮЛCreate, СвЮЛSerializer
from .utils import printProgressBar
from xml.etree.cElementTree import tostring
from datetime import datetime
import logging
from rest_framework import serializers
from django.conf import settings
import os


logs_dir = settings.LOGS_DIR
logs_file_name = "parse.log"

log = logging.getLogger('parse')
log.setLevel(logging.DEBUG)
ch = logging.FileHandler(filename=os.path.join(logs_dir, logs_file_name))
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)
# Create your models_ here.

#import logging
#log = logging.getLogger('parse')


class Файл(models.Model): # 4.1
    ТипИнф_choises = (
        ('ЕГРЮЛ_ОТКР_СВЕД', 'при передаче информации с открытыми сведениями (отсутствуют сведения о документах, удостоверяющих личность, и адресах физических лиц)'),
        ('ЕГРЮЛ_ЗАКР_СВЕД', 'при передаче информации с закрытыми сведениями (присутствуют сведения о документах, удостоверяющих личность, и адресах физических лиц)'),
    )
    ИдФайл = models.CharField(max_length=100, null=True, verbose_name='Файл')
    ВерсФорм = models.CharField(max_length=5, null=True, verbose_name='Версия формата')
    ТипИнф = models.CharField(max_length=50, null=True, choices=ТипИнф_choises, verbose_name='Тип информации')
    ВерсПрог = models.CharField(max_length=100, null=True, blank=True, verbose_name='Версия передающей программы')
    КолДок = models.IntegerField(null=True, verbose_name='Количество документов')
    ИдОтпр = models.ForeignKey(ИдОтпр, null=True, blank=True, verbose_name='Сведения об отправителе', on_delete=models.DO_NOTHING)
    size = models.IntegerField(null=True, verbose_name='Размер файла')

    def __str__(self):
        return '%s - %s' % (self.ИдФайл, self.id)


class ФайлCreate:
    def __init__(self, file, size):
        # print('tag=%s, attrib=%s' % (file.tag, file.attrib))
        # print('ИдФайл = %s' % (file.get('ИдФайл')))
        self.ИдФайл = file.get('ИдФайл')
        self.ВерсФорм = file.get('ВерсФорм')
        self.ТипИнф = file.get('ТипИнф')
        self.ВерсПрог = file.get('ВерсПрог')
        self.КолДок = file.get('КолДок')
        self.ИдОтпр = ИдОтпрCreate(file.find('ИдОтпр'))
        self.size = size
        self.a = Файл.objects.create(ИдФайл=self.ИдФайл, ВерсФорм=self.ВерсФорм, КолДок=int(self.КолДок),
                                     ТипИнф=self.ТипИнф, ВерсПрог=self.ВерсПрог, ИдОтпр=self.ИдОтпр.save(), size=size)
        self.Документы = [ДокументCreate(i, self.a) for i in file.findall('Документ')]
        if len(self.Документы) > 1:
            log.info('Find - %s Документы ' % str(len(self.Документы)))

    def save(self):
        self.a.save()
        i = len(self.Документы)
        j = 0
        for doc in self.Документы:
            j += 1
            printProgressBar(iteration=j, total=i)
            if doc.isGreated:
                doc.save()


class Документ(models.Model):

    AddDate = models.DateField(auto_now=True, null=False,
                               verbose_name='Дата добавления записи')
    ИдДок = models.CharField(max_length=36, null=True, verbose_name='Идентификатор документа')
    СвЮЛ = models.ForeignKey(СвЮЛ, null=True, verbose_name='Сведения о юридическом лице', on_delete=models.DO_NOTHING)
    СвЮЛ_XML = models.TextField(null=True, verbose_name='Сведения о юридическом лице в XML')
    Файл = models.ForeignKey(Файл, null=True, verbose_name='Файл с данными', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.ИдДок, self.id)

    content = [{
            "title": "Начало",
            "href": "top"},
            {
                "title": "Общие сведения",
                "href": "General"
            },
            {
                "title": "Сведения о наименовании юридического лица",
                "href": "Name"
            },
            {
                "title": "Сведения об адресе (месте нахождения)",
                "href": "Address"
            },
            {
                "title": "Сведения о регистрации (образовании) юридического лица",
                "href": "ObrUL"
            },
            {
                "title": "Сведения о регистрирующем органе по месту нахождения юридического лица",
                "href": "SvRegOrg"
            }
    ]
    content_СвЗапЕГРЮЛ = {
        "title": "Сведения о записях, внесенных в ЕГРЮЛ",
        "href": "EGRULrecords"}
    content_bottom = {
        "title": "Конец",
        "href": "bottom"}

    contents = [
        {'СвАдрЭлПочты': {"title": "Сведения об адресе электронной почты юридического лица",
                            "href": "Email"}},
        {'СвСтатус': {"title": "Сведения о состоянии (статусе) юридического лица",
                      "href": "SvStatus"}},
        {'СвПрекрЮЛ':   {"title": "Сведения о прекращении юридического лица",
                        "href": "SvPrekUl"}},
        {'СвУчетНО':    {"title": "Сведения об учете в налоговом органе",
                        "href": "SvUchN"}},
        {'СвРегПФ':     {"title": "Сведения о регистрации юридического лица в качестве страхователя в территориальном органе Пенсионного фонда Российской Федерации",
                        "href": "SvRegPF"}},
        {'СвРегФСС':    {"title": "Сведения о регистрации юридического лица в качестве страхователя в исполнительном органе Фонда социального страхования Российской Федерации",
                        "href": "SvRegFSS"}},
        {'СвУстКап':    {"title": "Сведения о размере указанного в учредительных документах коммерческой организации уставного капитала (складочного капитала, уставного фонда, паевого фонда)",
                        "href": "SvUstKap"}},
        {'СвТипУстав':  {"title": "Сведения об использовании юридическим лицом типового устава",
                        "href": "SvTipUS"}},
        {'СвУпрОрг':    {"title": "Сведения об управляющей организации",
                        "href": "SvUpOrg"}},
        {'СведДолжнФЛ': {"title": "Сведения о лице, имеющем право без доверенности действовать от имени юридического лица",
                        "href": "SvDoljFL"}},
        {'СвУчредит':   {"title": "Сведения об учредителях (участниках) юридического лица",
                        "href": "SvUchr"}},
        {'СвДоляООО': {"title": "Сведения о доле в уставном капитале общества с ограниченной ответственностью, принадлежащей обществу",
                       "href": "SvDolOOO"}},
        {'СвДержРеестрАО': {"title": "Сведения о держателе реестра акционеров акционерного общества",
            "href": "SvDerjReestrAO"}},
        {'СвОКВЭД':     {"title": "Сведения о видах экономической деятельности по Общероссийскому классификатору видов экономической деятельности",
                    "href": "SvOKWED"}},
        {'СвЛицензия':  {"title": "Сведения о лицензиях, выданных ЮЛ",
            "href": "SvLicense"}},
        {'СвПодразд': {"title": "Сведения об обособленных подразделениях юридического лица",
                        "href": "SvPodrazd"}},
        {'СвРеорг': {"title": "Сведения об участии в реорганизации",
                       "href": "SvReorg"}},
        {'СвПредш': {"title": "Сведения о правопредшественнике",
                     "href": "SvPredSh"}},
        {'СвКФХПредш': {"title": "Сведения о крестьянском (фермерском) хозяйстве, на базе имущества которого создано юридическое лицо",
                     "href": "SvKFHPredSh"}},
        {'СвКФХПредш': {
            "title": "Сведения о крестьянском (фермерском) хозяйстве, на базе имущества которого создано юридическое лицо",
            "href": "SvKFHPredSh"}},
        {'СвПреем': {
            "title": "Сведения о правопреемнике",
            "href": "SvPreem"}},
        {'СвКФХПреем': {
            "title": "Сведения о крестьянском (фермерском) хозяйстве, которые внесены в ЕГРИП в связи с приведением правового статуса крестьянского (фермерского) хозяйства в соответствие с нормами части первой Гражданского кодекса Российской Федерации",
            "href": "SvKFHPreem"}},
        ]

    def get_content(self):
        root = ET.fromstring(self.СвЮЛ_XML)
        my_content = self.content.copy()
        for item in self.contents:
            if root.find(list(item.keys())[0]):
                my_content.append(list(item.values())[0])

        my_content.append(self.content_СвЗапЕГРЮЛ)
        my_content.append(self.content_bottom)
        return my_content

    def get_info(self):
        return {'ogrn': self.СвЮЛ.ОГРН, "inn": self.СвЮЛ.ИНН, 'full_name':self.СвЮЛ.СвНаимЮЛ.НаимЮЛСокр, 'addr': self.СвЮЛ.СвАдресЮЛ.АдресРФ.Индекс}


class ДокументCreate:
    def __init__(self, document, file):
        self.ИдДок = document.get('ИдДок')
        self.СвЮЛ = СвЮЛCreate(document.find('СвЮЛ'))
        self.СвЮЛ_XML = tostring(document.find('СвЮЛ'), encoding='utf-8', method="xml").decode('utf-8')
        self.isGreated = False

        objects = Документ.objects.filter(СвЮЛ__ОГРН=self.СвЮЛ.ОГРН)
        if not objects:
            log.info('Greate new Документ witch OGRN - %s' % str(self.СвЮЛ.ОГРН))
            self.a = Документ.objects.create(ИдДок=self.ИдДок, СвЮЛ=self.СвЮЛ.save(), Файл=file,
                                              СвЮЛ_XML=self.СвЮЛ_XML)
            self.isGreated = True
        elif len(objects) == 1:
            log.info('One OGRN - %s, find in database' % str(self.СвЮЛ.ОГРН))
            doc = Документ.objects.get(СвЮЛ__ОГРН=self.СвЮЛ.ОГРН)
            # print(doc.СвЮЛ.ДатаВып.strftime('%Y-%m-%d'), self.СвЮЛ.ДатаВып)
            if doc.СвЮЛ.ДатаВып <= datetime.strptime(self.СвЮЛ.ДатаВып, '%Y-%m-%d').date():
                log.info('ДатаВып in XML %s is newer or equal than in the DB - %s, check quantity documents ' % (self.СвЮЛ.ДатаВып, doc.СвЮЛ.ДатаВып.strftime('%Y-%m-%d')))
                # log.info('КолЗапЕГРЮЛ in DB %s, in the XML - %s' % (
                #    doc.СвЮЛ.КолЗапЕГРЮЛ, self.СвЮЛ.КолЗапЕГРЮЛ))
                if doc.СвЮЛ.КолЗапЕГРЮЛ is not None:
                    if doc.СвЮЛ.КолЗапЕГРЮЛ >= self.СвЮЛ.КолЗапЕГРЮЛ:
                        log.info('WARN КолЗапЕГРЮЛ in DB %s is more or equal than in the XML - %s, NOT update DB Документ' % (
                            doc.СвЮЛ.КолЗапЕГРЮЛ, self.СвЮЛ.КолЗапЕГРЮЛ))
                    else:
                        log.info('КолЗапЕГРЮЛ in DB %s is less than in the XML - %s, APPLYING Update Документ' % (
                            doc.СвЮЛ.КолЗапЕГРЮЛ, self.СвЮЛ.КолЗапЕГРЮЛ))
                        doc.ИдДок = self.ИдДок
                        doc.СвЮЛ = self.СвЮЛ.save()
                        doc.Файл = file
                        doc.СвЮЛ_XML = self.СвЮЛ_XML
                        doc.save()
                else:
                    log.info('КолЗапЕГРЮЛ in the DB is - %s, in XML %s ' % (
                        doc.СвЮЛ.КолЗапЕГРЮЛ, self.СвЮЛ.КолЗапЕГРЮЛ))
                    #doc.delete()
                    #self.a = mДокумент.objects.create(ИдДок=self.ИдДок, СвЮЛ=self.СвЮЛ.save(), Файл=file,
                    #                                  СвЮЛ_XML=self.СвЮЛ_XML)
                    doc.ИдДок = self.ИдДок
                    doc.СвЮЛ = self.СвЮЛ.save()
                    doc.Файл = file
                    doc.СвЮЛ_XML = self.СвЮЛ_XML
                    doc.save()

            else:
                log.info('ДатаВып is older')
        elif len(objects) > 1:
            log.info('Check OGRN - %s, found %s. ERROR!!!!' % (str(self.СвЮЛ.ОГРН), str(len(objects))))
            # objects.delete()


    def save(self):
        if self.isGreated:
            self.a.save()


class ДокументSerializer(serializers.ModelSerializer):
    СвЮЛ = СвЮЛSerializer(many=False)

    class Meta:
        model = Документ
        fields = ('id', 'ИдДок', 'СвЮЛ',)


class Regions(models.Model):
    КодРегион = models.CharField(max_length=2, null=True, blank=True,
                              verbose_name='Код субъекта Российской Федерации')
    Регион = models.CharField(max_length=500,
                                verbose_name='Наименование субъекта Российской Федерации')

    def __str__(self):
        return '%s - %s' % (self.КодРегион, self.Регион)

    class Meta:
        ordering = ['КодРегион']


class RegionsSerializer(serializers.ModelSerializer):

    value = serializers.CharField(source='КодРегион', read_only=True)
    name = serializers.CharField(source='Регион', read_only=True)

    class Meta:
        model = Regions
        fields = ('value', 'name',)

class States(models.Model):
    КодСтатусЮЛ = models.CharField(max_length=3,
                                   verbose_name='Код статуса юридического лица по справочнику СЮЛСТ')
    НаимСтатусЮЛ = models.CharField(max_length=500,
                                verbose_name='Наименование статуса юридического лица по справочнику СЮЛСТ')

    def __str__(self):
        return '%s - %s' % (self.КодСтатусЮЛ, self.НаимСтатусЮЛ)

    class Meta:
        ordering = ['КодСтатусЮЛ']


class StatesSerializer(serializers.ModelSerializer):

    value = serializers.CharField(source='КодСтатусЮЛ', read_only=True)
    name = serializers.CharField(source='НаимСтатусЮЛ', read_only=True)

    class Meta:
        model = States
        fields = ('value', 'name',)


class ModeEducation(models.Model):
    КодСпОбрЮЛ = models.CharField(max_length=2, null=True, blank=True, verbose_name='Код способа образования по справочнику СЮЛНД')
    НаимСпОбрЮЛ = models.CharField(max_length=255, null=True,
                                   verbose_name='Наименование способа образования юридического лица')

    class Meta:
        ordering = [F('КодСпОбрЮЛ').asc(nulls_first=True)]


class ModeEducationSerializer(serializers.ModelSerializer):

    value = serializers.CharField(source='КодСпОбрЮЛ', read_only=True)
    name = serializers.CharField(source='НаимСпОбрЮЛ', read_only=True)

    class Meta:
        model = ModeEducation
        fields = ('value', 'name',)


class OKVED(models.Model):

    КодОКВЭД = models.CharField(max_length=8, null=True, blank=True,
                                verbose_name='Код по Общероссийскому классификатору видов экономической деятельности')
    НаимОКВЭД = models.CharField(max_length=1000, null=True, blank=True,
                                 verbose_name='Наименование вида деятельности по Общероссийскому классификатору видов экономической деятельности')
    ПрВерсОКВЭД = models.CharField(max_length=4, null=True, blank=True,
                                   verbose_name='Код по Общероссийскому классификатору видов экономической деятельности')

    def __str__(self):
        if self.ПрВерсОКВЭД == None:
            ПрВерсОКВЭД = '2001'
        else:
            ПрВерсОКВЭД = self.ПрВерсОКВЭД
        return '(%s) %s - %s' % (ПрВерсОКВЭД, self.КодОКВЭД, self.НаимОКВЭД)

    class Meta:
        ordering = ['КодОКВЭД']


class OKVEDSerializer(serializers.ModelSerializer):

    value = serializers.CharField(source='КодОКВЭД', read_only=True)
    name = serializers.CharField(source='НаимОКВЭД', read_only=True)
    ver = serializers.CharField(source='ПрВерсОКВЭД', read_only=True)

    class Meta:
        model = OKVED
        fields = ('value', 'name', 'ver',)


class FilterField(models.Model):

    type_choises = (
        ('Char', 'Текстовый'),
        ('Number', 'Числовой'),
        ('Date', 'Дата'),
        ('Select', 'Список'),
        ('MultipleSelect', 'Список с множественным выбором'),
        ('Bool', 'Выбор Да/Нет'),
    )
    options_choises = (
        ('OKVER', 'Справочник ОКВЭД'),
        ('ModeEDU', 'Справочник способов образования'),
        ('States', 'Справочник состояний'),
        ('Regions', 'Справочник регинов'),
        ('Capitals', 'Справочник видов капитала'),
    )

    name = models.CharField(max_length=20, null=False, blank=False,
                            verbose_name='Наименование поля для фильрации')
    sortBy = models.IntegerField(null=False, blank=False,
                            verbose_name='Номер для сортировки внутри блока')

    label = models.CharField(max_length=200, null=False, blank=False,
                             verbose_name='Отображаемое наименование')
    i_d = models.CharField(max_length=20, null=False, blank=False,
                           verbose_name='Идентификатор для связи метки')
    asPlaceholder = models.BooleanField(default=True, blank=False,
                                        verbose_name='Выводим подсказку как placeholder')
    type = models.CharField(max_length=20, null=False, choices=type_choises, verbose_name='Тип Фильтра')
    isFilter = models.BooleanField(default=True, blank=False,
                                        verbose_name='Признак фильра')
    options = models.CharField(max_length=10, blank=True, null=True, choices=options_choises, verbose_name='Опции фильтра')

    def __str__(self):
        return '%s - %s' % (self.name, self.label)




class FilterFieldSerializer(serializers.BaseSerializer):

    def to_representation(self, obj):

        if obj.options is None:
            options = None
        elif obj.options == 'Regions':
            options = RegionsSerializer(Regions.objects.all(), many=True).data
        elif obj.options == 'ModeEDU':
            options = ModeEducationSerializer(ModeEducation.objects.all(), many=True).data
        elif obj.options == 'States':
            options = StatesSerializer(States.objects.all(), many=True).data
        elif obj.options == 'OKVER':
            options = OKVEDSerializer(OKVED.objects.all(), many=True).data
        elif obj.options == 'Capitals':
            options = [{
                        'value': "",
                        'name': "Любой",
                    }, {
                        'value': "УСТАВНЫЙ КАПИТАЛ",
                        'name': "УСТАВНЫЙ КАПИТАЛ",
                    }, {
                        'value': "СКЛАДОЧНЫЙ КАПИТАЛ",
                        'name': "СКЛАДОЧНЫЙ КАПИТАЛ",
                    }, {
                        'value': "УСТАВНЫЙ ФОНД",
                        'name': "УСТАВНЫЙ ФОНД",
                    }, {
                        'value': "ПАЕВЫЕ ВЗНОСЫ",
                        'name': "ПАЕВЫЕ ВЗНОСЫ",
                    }, {
                        'value': "ПАЕВОЙ ФОНД",
                        'name': "ПАЕВОЙ ФОНД",
                    }]
        else:
            options = None

        return {
            'name': obj.name,
            'label': obj.label,
            'i_d': obj.i_d,
            'asPlaceholder': obj.asPlaceholder,
            'type': obj.type,
            'isFilter': obj.isFilter,
            'options': options
        }


class FilterBlock(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False,
                            verbose_name='Наименование блока для фильрации')
    sortBy = models.IntegerField(null=False, blank=False,
                                 verbose_name='Номер для блоков')
    label = models.CharField(max_length=200, null=False, blank=False,
                             verbose_name='Отображаемое наименование блока')
    i_d = models.CharField(max_length=20, null=False, blank=False,
                             verbose_name='Идентификатор для связи метки')
    isFilter = models.BooleanField(default=True, blank=False,
                                   verbose_name='Признак что сам блок является фильром')
    fields = models.ManyToManyField(FilterField, verbose_name='Поля для фильтрации')

    def __str__(self):
        return '%s - %s' % (self.name, self.label)

    class Meta:
        ordering = ['sortBy']


class FilterBlockSerializer(serializers.ModelSerializer):

    fields = FilterFieldSerializer(many=True)

    class Meta:
        model = FilterBlock
        fields = ('name', 'label', 'i_d', 'isFilter', 'fields', )
