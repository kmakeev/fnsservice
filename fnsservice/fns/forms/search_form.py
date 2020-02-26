from djng.styling.bootstrap3.forms import Bootstrap3Form
from djng.forms import NgModelFormMixin
from djng.forms import fields, NgDeclarativeFieldsMetaclass, NgFormValidationMixin
from fns.models import Regions, States, OKVED

class SearchForm_(Bootstrap3Form):


    BASE_CHOICES = [('egrul', 'ЕГРЮЛ'), ('egrip', 'ЕГРИП')]

    ACTIVE_CHOICES = [('', 'Все'),
                      ('False', 'Деятельность юридического лица прекращена'),
                      ('True', 'Действующее юридическое лицо или код статуса юридического лица по справочнику СЮЛСТ больше 200 и меньше 700'),
                      ]

    # base = fields.ChoiceField(label='Выберите реестр', initial='egrul', choices=BASE_CHOICES)
    search = fields.CharField(min_length=2, label='ОГРН, ИНН или наименование юридического лица', required=True,
                              error_messages={"invalid": "Доложно быть заполнено, минимум 2 символа"})
    fio = fields.CharField(min_length=2,
                              label='ФИО лица, являющегося руководителем, учредителем или участником ЮЛ',
                              required=False,
                              error_messages={"invalid": "Доложно быть заполнено, минимум 2 символа"})
    reg_start_date = fields.DateField(label='Дата начала постановки на учет:', required=False, input_formats=['%Y-%m-%d'])
    reg_end_date = fields.DateField(label='Дата окончания постановки на учет:', required=False, input_formats=['%Y-%m-%d'])
    #region = fields.ChoiceField(initial='', label='Регион', choices=REGION_CHOICES)
    region = fields.ModelChoiceField(empty_label='Любой', label='Регион', to_field_name='КодРегион', queryset=Regions.objects.all())
    isactive = fields.ChoiceField(initial='', label='Прекращение деятельности', choices=ACTIVE_CHOICES)
    #state = fields.ChoiceField(initial='', label='Cостояние (статус) юридического лица', choices=STATE_CHOICES)
    state = fields.ModelChoiceField(empty_label='Любое', label='Cостояние (статус) юридического лица', to_field_name='КодСтатусЮЛ',
                                     queryset=States.objects.all())
    okved = fields.ModelChoiceField(empty_label='Любое', label='Наименование вида деятельности по ОКВЭД',
                                    to_field_name='КодОКВЭД',
                                    queryset=OKVED.objects.all())


class SearchForm(NgModelFormMixin, SearchForm_):

    form_name = 'search_form'
    scope_prefix = 'subscribe_data'