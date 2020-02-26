from djng.styling.bootstrap3.forms import Bootstrap3Form
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django import forms
from djng.forms import NgModelFormMixin
from djng.forms import fields, NgDeclarativeFieldsMetaclass, NgFormValidationMixin

from fns.utils import check_ogrn


class GetOrderingForm_(Bootstrap3Form):

    TYPES_CHOICES = [('fo', 'Получение выписки, содержащей открытые сведения'),
                     ('fz', 'Получение выписки, содержащей закрытые сведения')]

    type = fields.ChoiceField(initial='fz', label='Выберите тип запроса', choices=TYPES_CHOICES)

    search = fields.CharField(min_length=13, label='ОГРН юридического лица', required=True,
                              error_messages={"invalid": "Параметр не является ОГРН"})


class GetOrderingForm(NgModelFormMixin, GetOrderingForm_):

    form_name = 'getOrdering_form'
    scope_prefix = 'getOrdering_data'

    def clean(self):
        print(self.cleaned_data)
        if 'search' in self.cleaned_data and 'type' in self.cleaned_data:
            search = self.cleaned_data['search']

            if not check_ogrn(search):
                raise ValidationError('Параметр не является ОГРН юридического лица', code='invalid')
        else:
            raise ValidationError('Параметр не является ОГРН юридического лица', code='invalid')
        return super(GetOrderingForm, self).clean()
