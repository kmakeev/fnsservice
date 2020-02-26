from djng.styling.bootstrap3.forms import Bootstrap3Form
from djng.forms import NgModelFormMixin
from djng.forms import fields, NgDeclarativeFieldsMetaclass, NgFormValidationMixin
from django.forms import widgets


class AdvancedSearchForm_(Bootstrap3Form):

    EDUMETODCODE_CHOICES = [('', 'Любой'),
                            ('01', 'Создание юридического лица до 01.07.2002'),
                            ('02', 'Создание юридического лица путем реорганизации до 01.07.2002'),
                            ('03',
                             'Регистрации на территории Республики Крым или территории города федерального значения Севастополя на день принятия в Российскую Федерацию '),
                            ('11', 'Создание юридического лица'),
                            ('21', 'Создание юридического лица путем реорганизации в форме преобразования'),
                            ('22', 'Создание юридического лица путем реорганизации в форме слияния'),
                            ('23', 'Создание юридического лица путем реорганизации в форме разделения'),
                            ('24', 'Создание юридического лица путем реорганизации в форме выделения'),
                            ('26',
                             'Создание юридического лица путем реорганизации в форме выделения с одновременным прекращением его деятельности в связи с присоединением к другому юридическому лицу'),
                            ('29',
                             'СОЗДАНИЕ ЮРИДИЧЕСКОГО ЛИЦА ПУТЕМ РЕОРГАНИЗАЦИИ В ФОРМЕ СЛИЯНИЯ ЮРИДИЧЕСКИХ ЛИЦ, ВКЛЮЧАЯ ЮРИДИЧЕСКОЕ ЛИЦО, ДЕЯТЕЛЬНОСТЬ КОТОРОГО ПРЕКРАЩАЕТСЯ ОДНОВРЕМЕННО С ЕГО СОЗДАНИЕМ ПРИ РЕОРГАНИЗАЦИИ ДРУГОГО ЮРИДИЧЕСКОГО ЛИЦА В ФОРМЕ РАЗДЕЛЕНИЯ'),
                            ('30', 'Создание юридического лица путем реорганизации'),
                           ]

    isaddr = fields.BooleanField(help_text='Сведения об адресе (месте нахождения)', required=False)
    isAddrFalsity = fields.BooleanField(help_text='Признак недостоверности адреса', required=False)
    isAddrChange = fields.BooleanField(help_text='Сведения о принятии юридическим лицом решения об изменении места нахождения', required=False)
    index = fields.CharField(required=False, widget=widgets.TextInput(attrs={'placeholder': 'Индекс'}))
    codeKLADR = fields.CharField(required=False, widget=widgets.TextInput(attrs={'placeholder': 'Код адреса по КЛАДР'}))
    area = fields.CharField(required=False, widget=widgets.TextInput(attrs={'placeholder': 'Район (улус и т.п.)'}))
    city = fields.CharField(required=False, widget=widgets.TextInput(attrs={'placeholder': 'Город (волость и т.п.)'}))
    locality = fields.CharField(required=False, widget=widgets.TextInput(attrs={'placeholder': 'Населенный пункт (село и т.п.)'}))
    street = fields.CharField(required=False, widget=widgets.TextInput(attrs={'placeholder': 'Улица (проспект, переулок и т.п.)'}))

    isemail = fields.BooleanField(help_text='Сведения об адресе электронной почты юридического лица', required=False)
    email = fields.CharField(required=False, widget=widgets.TextInput(attrs={'placeholder': 'E-mail'}))

    isRegInfo = fields.BooleanField(help_text='Сведения о регистрации (образовании) юридического лица ', required=False)
    regNum = fields.CharField(required=False, widget=widgets.TextInput(attrs={'placeholder': 'Номер, присвоенный ЮЛ до 1 июля 2002 года'}))
    codeEduMethod = fields.ChoiceField(initial='', label='Способ образования юридического лица', choices=EDUMETODCODE_CHOICES, widget=widgets.Select(attrs={'class': 'form-control-sm'}))

class AdvancedSearchForm(NgModelFormMixin,  AdvancedSearchForm_):

    form_name = ' AdvancedSearch_form'
    scope_prefix = 'advanced_subscribe_data'