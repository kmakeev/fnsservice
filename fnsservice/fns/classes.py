# -*- coding: utf8 -*-
import xml.etree.cElementTree as ET
from lxml import etree
from . models import Файл
from . models import ФайлCreate
import os
import logging
import threading
from queue import Queue
from django.db import connection

log = logging.getLogger('parse')

NUM_OF_THREADS = 10


class myMultiThread(threading.Thread):

    def __init__(self, queue, out_dir):
        threading.Thread.__init__(self)
        self.out_dir = out_dir
        self.queue = queue

    def run(self):
        while True:
            file = self.queue.get()
            self.parse_file(file)
            self.queue.task_done()

    def parse_file(self, full_file_patch):
        print('Parse file - ', full_file_patch)
        patch, file = os.path.split(full_file_patch)
        is_already_in_database = Файл.objects.filter(ИдФайл=os.path.splitext(file)[0], size=os.path.getsize(full_file_patch))
        if is_already_in_database:
            log.info('File - %s already in database' % file)
        else:
            obj = XmlERGUL(full_file_patch)
            obj.parse()
            connection.close()
        try:
            log.info('Remove file %s to out dir - %s' % (file, self.out_dir))
            os.rename(full_file_patch, os.path.join(self.out_dir, file))
        except:
            log.info('Error to remove file %s' % full_file_patch)


def parse_folder(folder_name, out_dir):
    queue = Queue()
    for i in range(NUM_OF_THREADS):
        th = myMultiThread(queue, out_dir)
        th.setDaemon(True)
        th.start()
    for name in os.listdir(folder_name):
        file = os.path.join(folder_name, name)
        if os.path.isfile(file):
            queue.put(file)
    queue.join()
    log.info('Parsing folder complete')


def xslt_process(xml_file, xsl_file):
    dom = etree.parse(xml_file)
    xslt = etree.parse(xsl_file)
    transform = etree.XSLT(xslt)
    newdom = transform(dom)
    return etree.tostring(newdom, pretty_print=True)


class XmlERGUL:

    def __init__(self, xml_file):
        self.tree = ET.ElementTree(file=xml_file)
        self.root = self.tree.getroot()
        self.xml_file = xml_file
        self.size = os.path.getsize(xml_file)

    def parse(self):
        file = ФайлCreate(self.root, self.size)
        log.info('Save file %s' % self.xml_file)
        file.save()



