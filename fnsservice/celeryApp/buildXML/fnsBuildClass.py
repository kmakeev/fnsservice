import zeep
from suds.client import Client as Client2
from lxml import etree as etree
from .FNSClasses import BaseXMLforRequest
import logging
import os
from django.conf import settings

xs = "http://www.w3.org/2001/XMLSchema"

el_name_with_ns = lambda ns: lambda el: '{%s}%s' % (ns, el)

logs_dir = settings.LOGS_DIR
logs_file_name = "sign.log"
out_xml_dir = logs_dir + "out_XML\\"

ch = logging.FileHandler(filename=os.path.join(logs_dir, logs_file_name))

log = logging.getLogger('sign')
log.setLevel(logging.DEBUG)
ch = logging.FileHandler(filename=os.path.join(logs_dir, logs_file_name))
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)

url = 'http://espep.arbitr.ru/espep/ESP.asmx?WSDL'
url_smev = 'http://94.125.90.50:6336/FNSEGRNSWS/FNSPubEGRService_24?wsdl'
wsuId = ''


class BaseFNSXML:

    def __init__(self, inn=None, ogrn=None, idreq=None, name='SendShortULRequest'):

        req = BaseXMLforRequest(inn=inn, ogrn=ogrn, name=name, idreq=idreq)
        self.obj_xml = etree.tostring(req.root,
                                      pretty_print=True,
                                      xml_declaration=True,
                                      encoding='UTF-8'
                                      )
        id_file_name = req.id
        self.file_name = id_file_name + ".xml"
        self.XMLfile_name = os.path.join(out_xml_dir, self.file_name)
        log.info('Init Base XML file to %s' % self.XMLfile_name)

    def getfile(self):
        try:
            with open(self.XMLfile_name, "wb") as xml_writer:
                xml_writer.write(self.obj_xml)
                xml_writer.close()
                log.info('Save created XML file %s' % str(self.XMLfile_name))
            return self.file_name
        except IOError:
            log.error('Error save created XML file %s' % str(self.XMLfile_name))
            return False
