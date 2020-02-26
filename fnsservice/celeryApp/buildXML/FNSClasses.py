import xml.etree.cElementTree as ET
from lxml import etree, objectify
import uuid
import datetime
import os
from django.conf import settings

soapenv = 'http://schemas.xmlsoap.org/soap/envelope/'
RequestPr = 'http://ws.unisoft/'
smev = 'http://smev.gosuslugi.ru/rev111111'
docprf_ShortULReq = 'http://ws.unisoft/EGRNXX/ShortULReq'
docprf_FullULReq = 'http://ws.unisoft/EGRNXX/FullULReq'
docprf_ShortFLReq = 'http://ws.unisoft/EGRNXX/ShortFLReq'
docprf_FullFLUL = 'http://ws.unisoft/EGRNXX/FullFLUL'
docprf_Response = 'http://ws.unisoft/EGRNXX/Response'
docprf_ResponseKSUL = 'http://ws.unisoft/EGRNXX/ResponseKSUL'
docprf_ResponseVIPUL = 'http://ws.unisoft/EGRNXX/ResponseVIPUL'
template_xml_dir = settings.TEMPLATES_XML_DIR
template_file_name = 'fns.xml'

el_name_with_ns = lambda ns: lambda el: '{%s}%s' % (ns, el)


class BaseResponseXML:

        def __init__(self, xml):

            XMLparser = etree.XMLParser()
            # tree = etree.parse(xml, XMLparser)
            self.root = etree.fromstring(xml, XMLparser)
            #print(etree.tostring(self.root))
            self.baseXML = Response(self.root)


class BaseXMLforRequest:

        def __init__(self, inn=None, ogrn=None, name=None, idreq=None, id=str(uuid.uuid4()), case_num='01'):
            XMLparser = etree.XMLParser()
            tree = etree.parse(os.path.join(template_xml_dir, template_file_name), XMLparser)
            self.root = tree.getroot()
            self.baseXML = Request(self.root)
            # id = "F0725D7C-2249-4443-B8FD-531DAF14B8D1"
            self.id = str(uuid.uuid4())
            if name == 'SendShortULRequest':
                req = etree.SubElement(self.baseXML.body.sendShort.messageData.appdata.doc, "ЗапросЮЛ",
                                       attrib={'ИдЗапрос': str(uuid.uuid4())})
                if ogrn:
                    ogrn_obj = etree.Element("ОГРН")
                    ogrn_obj.text = ogrn
                    req.append(ogrn_obj)
                if inn:
                    inn_obj = etree.Element("ИННЮЛ")
                    inn_obj.text = inn
                    req.append(inn_obj)
                self.baseXML.body.sendShort.messageData.appdata.doc.set('ИдДок', self.id)
                self.baseXML.body.sendShort.message.date.text = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
                self.baseXML.body.bodyETree.remove(self.baseXML.body.sendShortFL.shortFLRequest)
                self.baseXML.body.bodyETree.remove(self.baseXML.body.sendFull.fullRequest)
                self.baseXML.body.bodyETree.remove(self.baseXML.body.getShortUL.shortULResponse)
                self.baseXML.body.bodyETree.remove(self.baseXML.body.getFullUL.fullULResponse)
            elif name == 'SendShortFLRequest':
                pass
            elif name == 'SendFullULRequest':
                #print('Deleting ')
                req = etree.SubElement(self.baseXML.body.sendFull.messageData.appdata.doc, "ЗапросЮЛ")
                if ogrn:
                    ogrn_obj = etree.Element("ОГРН")
                    ogrn_obj.text = ogrn
                    req.append(ogrn_obj)
                self.baseXML.body.sendFull.messageData.appdata.doc.set('ИдДок', self.id)
                self.baseXML.body.sendFull.messageData.appdata.doc.set('НомерДела', case_num)
                self.baseXML.body.sendFull.message.date.text = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
                self.baseXML.body.bodyETree.remove(self.baseXML.body.sendShort.shortRequest)
                self.baseXML.body.bodyETree.remove(self.baseXML.body.sendShortFL.shortFLRequest)
                self.baseXML.body.bodyETree.remove(self.baseXML.body.getShortUL.shortULResponse)
                self.baseXML.body.bodyETree.remove(self.baseXML.body.getFullUL.fullULResponse)
            elif name == 'GetShortULResponse':
                if idreq:
                    self.baseXML.body.sendShort.messageData.appdata.doc.set('ИдЗапросФ', str(idreq))
                self.baseXML.body.sendShort.message.date.text = datetime.datetime.now().strftime(
                       "%Y-%m-%dT%H:%M:%SZ")
                self.baseXML.body.bodyETree.remove(self.baseXML.body.sendShort.shortRequest)
                self.baseXML.body.bodyETree.remove(self.baseXML.body.sendFull.fullRequest)
                self.baseXML.body.bodyETree.remove(self.baseXML.body.sendShortFL.shortFLRequest)
                self.baseXML.body.bodyETree.remove(self.baseXML.body.getFullUL.fullULResponse)
            elif name == 'GetFullULResponse':
                if idreq:
                    self.baseXML.body.getFullUL.messageData.appdata.doc.set('ИдЗапросФ', str(idreq))
                self.baseXML.body.getFullUL.message.date.text = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
                self.baseXML.body.bodyETree.remove(self.baseXML.body.sendShort.shortRequest)
                self.baseXML.body.bodyETree.remove(self.baseXML.body.sendFull.fullRequest)
                self.baseXML.body.bodyETree.remove(self.baseXML.body.sendShortFL.shortFLRequest)
                self.baseXML.body.bodyETree.remove(self.baseXML.body.getShortUL.shortULResponse)


class Appdata:
    def __init__(self, appdata, docprf):
        self.code = None
        self.id_req = None
        self.answer = None
        self.docprf = el_name_with_ns(docprf)
        self.doc = appdata.find(self.docprf('Документ'))
        if self.doc is not None:
            self.id_req = self.doc.get('ИдЗапросФ')
            self.code = self.doc.get('КодОбр')
            # print('Code in attr - ', self.code)
            # print('found code - ', self.doc.find(self.docprf('КодОбр')))
            if self.doc.find(self.docprf('КодОбр')) is not None:
                # print('Code in value - ', self.doc.find(self.docprf('КодОбр')).text)
                self.code = self.doc.find(self.docprf('КодОбр')).text
            self.answer = self.doc.find(self.docprf('Ответ'))
            if self.answer is not None:
                if self.answer.find(self.docprf('КодОбр')) is not None:
                    # print('Code in answer - ', self.answer.find(self.docprf('КодОбр')).text)
                    self.code = self.answer.find(self.docprf('КодОбр')).text
                else:
                    self.code = '00'
                    # print('Not code, - ', self.code)


class Message:
    def __init__(self, message):
        self.smev = el_name_with_ns(smev)
        self.message = message
        self.date = message.find(self.smev('Date'))
        self.status = message.find(self.smev('Status'))

class MessageData:
    def __init__(self, messageData, prf):
        self.smev = el_name_with_ns(smev)
        self.appdata = Appdata(messageData.find(self.smev('AppData')), docprf=prf)


class SendShortULRequestResponse:
    def __init__(self, shortRequestResponse):
        self.smev = el_name_with_ns(smev)
        self.messageData = MessageData(shortRequestResponse.find(self.smev('MessageData')), prf=docprf_Response)
        self.message = Message(shortRequestResponse.find(self.smev('Message')))


class SendFullULResponseResponse:
    def __init__(self, fullRequestResponse):
        self.smev = el_name_with_ns(smev)
        self.messageData = MessageData(fullRequestResponse.find(self.smev('MessageData')), prf=docprf_Response)
        self.message = Message(fullRequestResponse.find(self.smev('Message')))


class GetShortULResponseResponse:
    def __init__(self, shortResponseResponse):
        self.smev = el_name_with_ns(smev)
        self.messageData = MessageData(shortResponseResponse.find(self.smev('MessageData')), prf=docprf_ResponseKSUL)
        self.message = Message(shortResponseResponse.find(self.smev('Message')))


class GetFullULResponseResponse:
    def __init__(self, fullResponseResponse):
        self.smev = el_name_with_ns(smev)
        self.messageData = MessageData(fullResponseResponse.find(self.smev('MessageData')), prf=docprf_ResponseVIPUL)
        self.message = Message(fullResponseResponse.find(self.smev('Message')))


class SendShortULRequest:
    def __init__(self, shortRequest):
        self.smev = el_name_with_ns(smev)
        self.shortRequest = shortRequest
        self.messageData = MessageData(shortRequest.find(self.smev('MessageData')), prf=docprf_ShortULReq)
        self.message = Message(shortRequest.find(self.smev('Message')))


class SendFullULRequest:
    def __init__(self, fullRequest):
        self.smev = el_name_with_ns(smev)
        self.fullRequest = fullRequest
        self.messageData = MessageData(fullRequest.find(self.smev('MessageData')), prf=docprf_FullULReq)
        self.message = Message(fullRequest.find(self.smev('Message')))


class SendShortFLRequest:
    def __init__(self, shortFLRequest):
        self.smev = el_name_with_ns(smev)
        self.shortFLRequest = shortFLRequest
        self.messageData = MessageData(shortFLRequest.find(self.smev('MessageData')), prf=docprf_ShortFLReq)
        self.message = Message(shortFLRequest.find(self.smev('Message')))


class GetShortULResponse:
    def __init__(self, fullFLUL):
        self.smev = el_name_with_ns(smev)
        self.shortULResponse = fullFLUL
        self.messageData = MessageData(fullFLUL.find(self.smev('MessageData')), prf=docprf_FullFLUL)
        self.message = Message(fullFLUL.find(self.smev('Message')))


class GetFullULResponse:
    def __init__(self, fullFLUL):
        self.smev = el_name_with_ns(smev)
        self.fullULResponse = fullFLUL
        self.messageData = MessageData(fullFLUL.find(self.smev('MessageData')), prf=docprf_FullFLUL)
        self.message = Message(fullFLUL.find(self.smev('Message')))


class Body:
    def __init__(self, body):
        self.prefix = el_name_with_ns(RequestPr)
        self.bodyETree = body
        self.sendShort = SendShortULRequest(body.find(self.prefix('SendShortULRequest')))
        self.sendShortFL = SendShortFLRequest(body.find(self.prefix('SendShortFLRequest')))
        self.getShortUL = GetShortULResponse(body.find(self.prefix('GetShortULResponse')))
        self.sendFull = SendFullULRequest(body.find(self.prefix('SendFullULRequest')))
        self.getFullUL = GetFullULResponse(body.find(self.prefix('GetFullULResponse')))

class ResponseBody:
    def __init__(self, body):
        self.bodyETree = body
        self.prefix = el_name_with_ns(RequestPr)
        if body.find(self.prefix('SendShortULRequestResponse')) is not None:
            self.data = SendShortULRequestResponse(body.find(self.prefix('SendShortULRequestResponse')))
        elif body.find(self.prefix('GetShortULResponseResponse')) is not None:
            self.data = GetShortULResponseResponse(body.find(self.prefix('GetShortULResponseResponse')))
        elif body.find(self.prefix('SendFullULRequestResponse')) is not None:
            self.data = SendFullULResponseResponse(body.find(self.prefix('SendFullULRequestResponse')))
        elif body.find(self.prefix('GetFullULResponseResponse')) is not None:
            self.data = GetFullULResponseResponse(body.find(self.prefix('GetFullULResponseResponse')))


class Request:

    def __init__(self, root):
        self.soap = el_name_with_ns(soapenv)
        self.body = Body(root.find(self.soap('Body')))


class Response:

    def __init__(self, root):
        self.soap = el_name_with_ns(soapenv)
        self.body = ResponseBody(root.find(self.soap('Body')))
