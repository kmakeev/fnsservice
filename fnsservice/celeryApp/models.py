from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Request(models.Model):

    response_code = (
        ('01', 'Запрашиваемые сведения не найдены'),
        ('51', 'Запрос принят в обработку'),
        ('52', 'Ответ не готов'),
        ('53', 'Сведения не могут быть предоставлены в электронном виде'),
        ('82', 'Ошибка форматно-логического контроля'),
        ('83', 'Отсутсвует запрос с указанным идентификатором и видом запрошенных сведений'),
        ('97', 'Ошибка сохранения файла'),
        ('98', 'Ошибка проверки подписи сообщения'),
        ('99', 'Системная ошибка'),

    )

    datereq = models.DateTimeField(auto_now=True, null=False,
                               verbose_name='Дата, время добавления записи')
    idreq = models.CharField(max_length=100, null=True, verbose_name='Идентификатор запроса')
    service = models.CharField(max_length=50, null=False, verbose_name='Наименование сервиса')
    method = models.CharField(max_length=50, null=False, verbose_name='Наименованеи метода')
    code = models.CharField(max_length=2, null=True, choices=response_code, verbose_name='Код возврата')
    notsignfilename = models.CharField(max_length=100, null=True, verbose_name='Имя первоначально сгенерированного файла')
    reqfilename = models.CharField(max_length=100, null=True, verbose_name='Имя файла, содержащего запрос')
    resfilename = models.CharField(max_length=100, null=True, verbose_name='Имя файла, содержащего ответ')
    params = models.CharField(max_length=250, null=True, verbose_name='Параметры запроса')
    dateres = models.DateTimeField(auto_now=False, null=True,
                               verbose_name='Дата, время добавления ответа')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.DO_NOTHING)

    root_id = models.UUIDField(default=uuid.uuid4, null=True, verbose_name='Идентификатор первой задачи в цепочке')
    this_id = models.UUIDField(default=uuid.uuid4, null=True, verbose_name='Идентификатор выполняемой задачи, саздашей запись в БД')


    def __str__(self):
        return '%s(%s) - %s' % (self.idreq, self.params, self.code)

    class Meta:
        ordering = ['datereq']
        indexes = [
            models.Index(fields=['idreq', 'root_id', 'this_id', 'method',])
        ]


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = ('idreq', 'datereq', 'service', 'method', 'code', 'notsignfilename', 'reqfilename',
                  'resfilename', 'params', 'dateres', 'root_id', 'this_id',)