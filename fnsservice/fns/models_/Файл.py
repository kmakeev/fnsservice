from django.db import models
from .ИдОтпр import ИдОтпр, ИдОтпрCreate
from ..models import Документ
from ..models_.СвЮЛ import СвЮЛ, СвЮЛCreate
from ..utils import printProgressBar
from xml.etree.cElementTree import tostring
from datetime import datetime
import logging
# from .. log import Log

log = logging.getLogger('parse')
log.setLevel(logging.DEBUG)
ch = logging.FileHandler(filename='parse.log')
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)

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

    def __str__(self):
        return '%s - %s' % (self.ИдФайл, self.id)


class ДокументCreate:
    def __init__(self, document, file):
        self.ИдДок = document.get('ИдДок')
        self.СвЮЛ = СвЮЛCreate(document.find('СвЮЛ'))
        self.СвЮЛ_XML = tostring(document.find('СвЮЛ'), encoding='utf-8', method="xml")
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
                log.info('ДатаВып in XML %s is newer than in the DB - %s,  update Документ' % (doc.СвЮЛ.ДатаВып.strftime('%Y-%m-%d'), self.СвЮЛ.ДатаВып))

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


class ФайлCreate:
    def __init__(self, file):
        # print('tag=%s, attrib=%s' % (file.tag, file.attrib))
        # print('ИдФайл = %s' % (file.get('ИдФайл')))
        self.ИдФайл = file.get('ИдФайл')
        self.ВерсФорм = file.get('ВерсФорм')
        self.ТипИнф = file.get('ТипИнф')
        self.ВерсПрог = file.get('ВерсПрог')
        self.КолДок = file.get('КолДок')
        self.ИдОтпр = ИдОтпрCreate(file.find('ИдОтпр'))
        self.a = Файл.objects.create(ИдФайл=self.ИдФайл, ВерсФорм=self.ВерсФорм, КолДок=int(self.КолДок),
                                     ТипИнф=self.ТипИнф, ВерсПрог=self.ВерсПрог, ИдОтпр=self.ИдОтпр.save())
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
