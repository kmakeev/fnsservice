from __future__ import absolute_import, unicode_literals
import os
from fnsservice.celery import app
import logging
from .buildXML.fnsBuildClass import BaseFNSXML
from .buildXML.FNSClasses import BaseResponseXML
import zeep
from suds.client import Client as Client2
from django.conf import settings
import datetime
from .models import Request
from requests.exceptions import RequestException

from django.contrib.auth.models import User

import json

from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage

log = logging.getLogger('celery_task')
url_bad = 'http://espep.arbitrcv.ru/espep/ESP.asmx?WSDL'
# url = 'http://espep.arbitr.ru/espep/ESP.asmx?WSDL'
url = 'http://192.168.100.42/espep/ESP.asmx?WSDL'
url_smev = 'http://94.125.90.50:6336/FNSEGRNSWS/FNSPubEGRService_24?wsdl'
url_smev_p = 'http://172.16.90.14:7777/gateway/services/SID0003525/wsdl'
wsuId = ''

countdowns = [5, 60, 300, 600, 1200, 3600, 18000, 86400.0, 172800.0, 432000000.0]

TASK_EXPIRY = datetime.datetime.now() + datetime.timedelta(days=6)
TASK_TIME_OUT = 60
MAX_RETRIES = 10

logs_dir = settings.LOGS_DIR
out_xml_dir = logs_dir + "out_XML\\"
in_xml_dir = logs_dir + "in_XML\\"

#Для тестов

# user = User.objects.using('req').get(id=3)


@app.task(bind=True, max_retries=MAX_RETRIES, expires=TASK_EXPIRY, time_limit=TASK_TIME_OUT)
def newCreateXML(self, params):
    p_inn = None
    p_ogrn = None
    if params and 'name' in params:
        name = params['name']
        if 'user' in params:
            user_id = int(params['user'])
        else:
            return False
        try:
            user = User.objects.using('req').get(id=user_id)
            print(user)
        except:
            log.error('Error get user with id - %s' % (user_id))
            return False
        if name == 'SendShortULRequest':
            if 'inn' in params:
                p_inn = params['inn']
            elif 'ogrn' in params:
                p_ogrn = params['ogrn']
            log.info('create XML %s request with parameters inn - %s , ogrn - %s' % (name, p_inn, p_ogrn))
            xml = BaseFNSXML(inn=p_inn, ogrn=p_ogrn, name=name)
            if xml:
                log.info('Save root_id - %s , parent_id - %s, id - %s' % (self.request.root_id, self.request.parent_id, self.request.root_id))
                request = Request(service='SID003525', method=name, notsignfilename=xml.getfile(),
                                  params=params, user=user, root_id=self.request.root_id, this_id=self.request.id)
                request.save(using='req')
                return request.id
        elif name == 'SendShortFLRequest':
            #Запрос  кратких сведений по ИП
            pass
        elif name == 'SendFullULRequest':
            if 'ogrn' in params:
                p_ogrn = params['ogrn']
            log.info('create XML %s request with parameters inn - %s , ogrn - %s' % (name, p_inn, p_ogrn))
            xml = BaseFNSXML(inn=p_inn, ogrn=p_ogrn, name=name)
            if xml:
                log.info('Save root_id - %s , parent_id - %s, id - %s' % (
                self.request.root_id, self.request.parent_id, self.request.root_id))
                request = Request(service='SID003525', method=name, notsignfilename=xml.getfile(),
                                  params=params, user=user, root_id=self.request.root_id, this_id=self.request.id)
                request.save(using='req')
                return request.id

        elif name == 'GetShortULResponse':
            log.info('create XML %s request with parameters inn - %s , ogrn - %s' % (name, p_inn, p_ogrn))
            if 'id' in params:
                try:
                    request = Request.objects.using('req').get(id=params['id'])
                except Request.DoesNotExist as exc:
                    log.error('Error in get request from database id- %s' % (params['id']))
                    return False
                if request.code == '51':
                    xml = BaseFNSXML(idreq=request.idreq, name=name)
                    if xml:
                        log.info('Save root_id - %s , parent_id - %s, id - %s' % (
                        self.request.root_id, self.request.parent_id, self.request.root_id))
                        request = Request(service='SID003525', method=name, notsignfilename=xml.getfile(),
                                          params=params, user=user, root_id=self.request.root_id, this_id=self.request.id)
                        request.save(using='req')
                        return request.id
                else:
                    log.info('Response code in prev request id - %s is not 51 - %s ' % (id, request.code))
        elif name == 'GetFullULResponse':
            log.info('create XML %s request with parameters inn - %s , ogrn - %s' % (name, p_inn, p_ogrn))
            if 'id' in params:
                try:
                    request = Request.objects.using('req').get(id=params['id'])
                except Request.DoesNotExist as exc:
                    log.error('Error in get request from database id- %s' % (params['id']))
                    return False
                if request.code == '51':
                    xml = BaseFNSXML(idreq=request.idreq, name=name)
                    if xml:
                        log.info('Save root_id - %s , parent_id - %s, id - %s' % (
                        self.request.root_id, self.request.parent_id, self.request.root_id))
                        request = Request(service='SID003525', method=name, notsignfilename=xml.getfile(),
                                          params=params, user=user, root_id=self.request.root_id, this_id=self.request.id)
                        request.save(using='req')
                        return request.id
                else:
                    log.info('Response code in prev request id - %s is not 51 - %s ' % (id, request.code))

    log.error('Error create XML with parameters inn - %s' % (params))
    return False

@app.task
def createXML(params):
    p_inn = None
    p_ogrn = None
    if params and 'name' in params:
        name = params['name']
        if 'user' in params:
            user_id = int(params['user'])
        else:
            return False
        try:
            user = User.objects.using('req').get(id=user_id)
            print(user)
        except:
            log.error('Error get user with id - %s' % (user_id))
            return False
        if name == 'SendShortULRequest':
            if 'inn' in params:
                p_inn = params['inn']
            elif 'ogrn' in params:
                p_ogrn = params['ogrn']
            log.info('create XML %s request with parameters inn - %s , ogrn - %s' % (name, p_inn, p_ogrn))
            xml = BaseFNSXML(inn=p_inn, ogrn=p_ogrn, name=name)
            if xml:
                log.info('Save root_id - %s , id - %s' % (self.request.root_id, self.request.root_id))
                request = Request(service='SID003525', method=name, notsignfilename=xml.getfile(),
                                  params=params, user=user)
                request.save(using='req')
                return request.id
        elif name == 'SendShortFLRequest':
            #Запрос  кратких сведений по ИП
            pass
        elif name == 'SendFullULRequest':
            if 'ogrn' in params:
                p_ogrn = params['ogrn']
            log.info('create XML %s request with parameters inn - %s , ogrn - %s' % (name, p_inn, p_ogrn))
            xml = BaseFNSXML(inn=p_inn, ogrn=p_ogrn, name=name)
            if xml:
                log.info('Save root_id - %s , id - %s' % (self.request.root_id, self.request.root_id))
                request = Request(service='SID003525', method=name, notsignfilename=xml.getfile(),
                                  params=params, user=user)
                request.save(using='req')
                return request.id

        elif name == 'GetShortULResponse':
            log.info('create XML %s request with parameters inn - %s , ogrn - %s' % (name, p_inn, p_ogrn))
            if 'id' in params:
                try:
                    request = Request.objects.using('req').get(id=params['id'])
                except Request.DoesNotExist as exc:
                    log.error('Error in get request from database id- %s' % (params['id']))
                    return False
                if request.code == '51':
                    xml = BaseFNSXML(idreq=request.idreq, name=name)
                    if xml:
                        log.info('Save root_id - %s , id - %s' % (self.request.root_id, self.request.root_id))
                        request = Request(service='SID003525', method=name, notsignfilename=xml.getfile(),
                                          params=params, user=user)
                        request.save(using='req')
                        return request.id
                else:
                    log.info('Response code in prev request id - %s is not 51 - %s ' % (id, request.code))
        elif name == 'GetFullULResponse':
            log.info('create XML %s request with parameters inn - %s , ogrn - %s' % (name, p_inn, p_ogrn))
            if 'id' in params:
                try:
                    request = Request.objects.using('req').get(id=params['id'])
                except Request.DoesNotExist as exc:
                    log.error('Error in get request from database id- %s' % (params['id']))
                    return False
                if request.code == '51':
                    xml = BaseFNSXML(idreq=request.idreq, name=name)
                    if xml:
                        log.info('Save root_id - %s , id - %s' % (self.request.root_id, self.request.root_id))
                        request = Request(service='SID003525', method=name, notsignfilename=xml.getfile(),
                                          params=params, user=user)
                        request.save(using='req')
                        return request.id
                else:
                    log.info('Response code in prev request id - %s is not 51 - %s ' % (id, request.code))

    log.error('Error create XML with parameters inn - %s' % (params))
    return False


#autoretry_for=(RequestException, Request.DoesNotExist, IOError),retry_jitter=1
@app.task(bind=True, max_retries=MAX_RETRIES, expires=TASK_EXPIRY, time_limit=TASK_TIME_OUT)
          #retry_kwargs={'max_retries': 3})
def signXML(self, id):

    if id:
        retry = self.request.retries
        try:
            request = Request.objects.using('req').get(id=id)
        except Request.DoesNotExist as exc:
            log.error('Error in get request from database id- %s' % (id))
            return False
        file_name = request.notsignfilename
        full_file_name = os.path.join(out_xml_dir, file_name)
        log.info('Read and sign XML file - %s ' % full_file_name)

        # filename = "C:\\Python34\\ergul\\logs\out_XML\\a608bb0c-994b-4df3-9abf-0a515631b485.xml"
        try:
            obj_xml = open(full_file_name, 'rb').read()
        except IOError as exc:
            log.error('Error read XML file %s ' % full_file_name)
            if retry < MAX_RETRIES:
                raise self.retry(exc=exc)
            else:
                request.code = '97'
                request.save(using='req')
                return False

        try:
            client_for_sign = zeep.Client(url)
            resp = client_for_sign.service.SignXml(xmlData=obj_xml, wsuId=wsuId)
            log.info('Sign created XML file %s' % full_file_name)
        except RequestException as exc:
            log.error('Error sign XML file %s' % full_file_name)
            if retry < MAX_RETRIES:
                raise self.retry(exc=exc, countdown=countdowns[retry])
            else:
                request.code = '97'
                request.save(using='req')
                return False
        sign_xml = resp['SignedXml']

        #(patch, name) = os.path.split(str(file_name))
        sign_file_name = "sig-" + file_name
        sign_full_file_name = os.path.join(out_xml_dir, sign_file_name)
        #print(sign_XMLfile_name)
        #log.error('created name for sign XML file %s' % sign_XMLfile_name)
        try:
            with open(sign_full_file_name, "wb") as xml_writer:
                xml_writer.write(sign_xml)
                xml_writer.close()
                log.info('Save signed XML file %s' % sign_full_file_name)
        except IOError as exc:
            log.error('Error save signed XML file %s ' % sign_full_file_name)
            if retry < MAX_RETRIES:
                raise self.retry(exc=exc)
            else:
                request.code = '97'
                request.save(using='req')
                return False
        request.reqfilename = sign_file_name
        request.save(using='req')
        return id
    else:
        log.error('Not id in signXML params ')
        return False


@app.task(bind=True, max_retries=MAX_RETRIES, expires=TASK_EXPIRY, time_limit=TASK_TIME_OUT)
def sendFirstRequest(self, id):

    if id:
        retry = self.request.retries
        try:
            request = Request.objects.using('req').get(id=id)
        except:
            log.error('Error in get request from database id- %s' % (id))
            return False
        file_name = request.reqfilename
        full_file_name = os.path.join(out_xml_dir, file_name)
        # log.info('Read sign XML file - %s from database with id - $s, %s' % (full_file_name, id, file_name))
        log.info('Read sign XML file - %s , preparation to send first request' % full_file_name)
        try:
            sign_xml = open(full_file_name, 'rb').read()
        except IOError as exc:
            log.error('Error read sign XML file %s ' % full_file_name)
            if retry < MAX_RETRIES:
                raise self.retry(exc=exc, countdown=countdowns[retry])
            else:
                request.code = '97'
                request.save(using='req')
                return False
        #request = Request.objects.create(service='SID003525', method='SendShortULRequest', reqfilename=full_file_name, params='test')
        #request.save(using='req')
        try:
            client = Client2(url_smev, retxml=True)
        except Exception as exc:
            log.error('Error send request  %s' % str(exc))
            if retry < MAX_RETRIES:
                raise self.retry(exc=exc, countdown=countdowns[retry])
            else:
                request.code = '97'
                request.save(using='req')
                return False
        if request.method == 'SendShortULRequest':
            try:
                resp_xml = client.service.SendShortULRequest(__inject={'msg': sign_xml})
            except Exception as exc:
                log.error('Error send request  %s' % str(exc))
                if retry < MAX_RETRIES:
                    raise self.retry(exc=exc, countdown=countdowns[retry])
                else:
                    request.code = '97'
                    request.save(using='req')
                    return False
        elif request.method == 'SendFullULRequest':
            try:
                resp_xml = client.service.SendFullULRequest(__inject={'msg': sign_xml})
            except Exception as exc:
                log.error('Error send request  %s' % str(exc))
                if retry < MAX_RETRIES:
                    raise self.retry(exc=exc, countdown=countdowns[retry])
                else:
                    request.code = '97'
                    request.save(using='req')
                    return False
        XML_in_file_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-") + file_name
        full_XML_in_file_name = os.path.join(in_xml_dir, XML_in_file_name)
        try:
            with open(full_XML_in_file_name, "wb") as xml_writer:
                xml_writer.write(resp_xml)
                xml_writer.close()
                log.info('Save received XML file %s' % str(full_XML_in_file_name))
                res = BaseResponseXML(resp_xml)
                # print(str(res.baseXML.body.sendShort.messageData.appdata.doc.attrib['ИдЗапросФ']))
                # print(str(res.baseXML.body.sendShort.messageData.appdata.doc.attrib['КодОбр']))
                #print(str(res.baseXML.body.sendShort.messageData.appdata.doc.attrib['ИдДок']))
                request.idreq = str(res.baseXML.body.data.messageData.appdata.id_req)
                request.code = str(res.baseXML.body.data.messageData.appdata.code)
                # request.code = str(res.baseXML.body.data.messageData.appdata.doc.attrib['КодОбр'])
                #request.idreq = str(res.baseXML.body.data.messageData.appdata.doc.attrib['ИдЗапросФ'])
                request.resfilename = XML_in_file_name
                request.dateres = datetime.datetime.now()
                request.root_id = self.request.root_id
                request.this_id = self.request.id
                request.save(using='req')
                log.info('Save in base %s' % request)
                if request.code != '51':
                    log.error('Code in response first request is not 51 ')
                    if retry < MAX_RETRIES:
                        new_request = request
                        new_request.pk = None  # copying object
                        new_request.code = None
                        new_request.dateres = None
                        new_request.resfilename = None
                        new_request.save(using='req')
                        self.request.args[0] = new_request.id
                        log.info('Retry request witch id - %s ' % str(self.request.args[0]))
                        self.retry(countdown=countdowns[retry])
                        # повтор с новыми параметрами до принятия запроса в обработку

                params = {'id': id, 'user': request.user.id, 'name': request.method}
                if request.method == 'SendShortULRequest':
                    params['name'] = 'GetShortULResponse'
                elif request.method == 'SendFullULRequest':
                    params['name'] = 'GetFullULResponse'
                else:
                    pass
                log.info('Generete params for first request in base %s' % params)
        except IOError as exc:
            log.error('Error save received XML file %s' % str(XML_in_file_name))
            if retry < MAX_RETRIES:
                raise self.retry(exc=exc, countdown=countdowns[retry])
            else:
                request.code = '97'
                request.save(using='req')
                return False
        return params
    else:
        log.info('Not received XML in send first request task id - %s ' % id)
        return False

@app.task(bind=True, max_retries=MAX_RETRIES, expires=TASK_EXPIRY, time_limit=TASK_TIME_OUT)

def sendRequest(self, id):

    if id:
        retry = self.request.retries
        try:
            request = Request.objects.using('req').get(id=id)
        except:
            log.error('sendRequest:  Error in get request from database id- %s' % (id))
            return False
        file_name = request.reqfilename
        full_file_name = os.path.join(out_xml_dir, file_name)
        # log.info('Read sign XML file - %s from database with id - $s, %s' % (full_file_name, id, file_name))
        log.info('Read sign XML file - %s , preparation to send next request' % full_file_name)
        try:
            sign_xml = open(full_file_name, 'rb').read()
        except IOError as exc:
            log.error('Error read sign XML file %s ' % full_file_name)
            if retry < MAX_RETRIES:
                raise self.retry(exc=exc, countdown=countdowns[retry])
            else:
                request.code = '97'
                request.save(using='req')
                return False
        # request = Request.objects.create(service='SID003525', method='SendShortULRequest', reqfilename=full_file_name, params='test')
        # request.save(using='req')
        try:
            client = Client2(url_smev, retxml=True)

            if request.method == 'GetShortULResponse':
                try:
                    resp_xml = client.service.GetShortULResponse(__inject={'msg': sign_xml})
                except Exception as exc:
                    log.error('Error send request  %s' % str(exc))
                    if retry < MAX_RETRIES:
                        raise self.retry(exc=exc, countdown=countdowns[retry])
                    else:
                        request.code = '97'
                        request.save(using='req')
                        return False
            elif request.method == 'GetFullULResponse':
                try:
                    resp_xml = client.service.GetFullULResponse(__inject={'msg': sign_xml})
                except Exception as exc:
                    log.error('Error send request  %s' % str(exc))
                    if retry < MAX_RETRIES:
                        raise self.retry(exc=exc, countdown=countdowns[retry])
                    else:
                        request.code = '97'
                        request.save(using='req')
                        return False
            else:
                log.error('Unsupported request type in database id -  ' % (id))
                return False
            # прочие
        except Exception as exc:
            log.error('Error send request  %s' % str(exc))
            if retry < MAX_RETRIES:
                raise self.retry(exc=exc, countdown=countdowns[retry])
            else:
                request.code = '97'
                request.save(using='req')
                return False
        XML_in_file_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-") + file_name
        full_XML_in_file_name = os.path.join(in_xml_dir, XML_in_file_name)
        try:
            with open(full_XML_in_file_name, "wb") as xml_writer:
                xml_writer.write(resp_xml)
                xml_writer.close()
                log.info('Save received XML file %s' % str(full_XML_in_file_name))
                res = BaseResponseXML(resp_xml)
                # print(str(res.baseXML.body.data.messageData.appdata.doc.attrib['ИдЗапросФ']))
                request.resfilename = XML_in_file_name
                request.dateres = datetime.datetime.now()
                # print(res.baseXML.body.data.messageData.appdata.id_req)
                # print(res.baseXML.body.data.messageData.appdata.code)
                # request.idreq = str(res.baseXML.body.data.messageData.appdata.id_req)
                request.code = str(res.baseXML.body.data.messageData.appdata.code)
                request.root_id = self.request.root_id
                request.this_id = self.request.id
                request.save(using='req')
                log.info('Save in base from send_request %s' % request)
                # print('Request: args',  self.request.args)
                if request.code == '52':
                    log.error('Code in response 52, answer is not ready')
                    if retry < MAX_RETRIES:
                        new_request = request
                        new_request.pk = None  # copying object
                        new_request.code = None
                        new_request.dateres = None
                        new_request.resfilename = None
                        new_request.save(using='req')
                        self.request.args[0] = new_request.id
                        log.info('Retry request witch id - %s ' % str(self.request.args[0]))
                        self.retry(countdown=countdowns[retry])
                        # повтор с новыми параметрами до принятия запроса в обработку

        except IOError as exc:
            log.error('Error save received XML file %s' % str(XML_in_file_name))
            if retry < MAX_RETRIES:
                raise self.retry(exc=exc, countdown=countdowns[retry])
            else:
                request.code = '97'
                request.save(using='req')
                return False
        return True
    else:
        log.info('Not received XML in send request task id - %s ' % id)
        return False


@app.task(bind=True)
def debug_task(self, params):
    print('Request: {0!r}'.format(self.request))
    return params


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(30.0, check_update.s(), name='add every 30 sec')


@app.task(bind=True)
def check_update(self):
    try:
        user = User.objects.using('req').get(id=3)
    except:
        return False

    redis_publisher = RedisPublisher(facility='ws_user', users=[user.username])
    count_in_progress = Request.objects.using('req').filter(user=user, method__in=['GetFullULResponse', 'GetShortULResponse'], code__in=['52']).order_by(
        'root_id').distinct('root_id').count()
    count_in_resolved = Request.objects.using('req').filter(code__in=['01', '53', '82', '83', '97', '98', '99']).order_by('root_id').distinct(
                'root_id').count()
    log.info('Send on ws update progress - %s, resolved - %s' % (count_in_progress, count_in_resolved))
    dict = {'in_progress': count_in_progress, 'new_result': count_in_resolved}
    message = RedisMessage(json.dumps(dict))
    redis_publisher.publish_message(message)


