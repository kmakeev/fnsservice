from djng.styling.bootstrap3.forms import Bootstrap3Form
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django import forms
from djng.forms import NgModelFormMixin
from djng.forms import fields, NgDeclarativeFieldsMetaclass, NgFormValidationMixin


class InputForm_(Bootstrap3Form):

    search = fields.CharField(min_length=2, label='Для поиска необходимо ввести ОГРН или ИНН юридического лица либо указать наименование', required=True,
                              error_messages={"invalid": "Доложно быть заполнено, минимум 2 символа"})

class InputForm(NgModelFormMixin, InputForm_):

    form_name = 'search_form'
    scope_prefix = 'subscribe_data'

