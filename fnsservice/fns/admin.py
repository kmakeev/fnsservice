from django.contrib import admin
from .models import СвЮЛ, Файл, Документ, Regions, FilterBlock, FilterField, ModeEducation
from .models_.ГРНДатаТип import ГРНДатаТип
from .models_.АдрРФЕГРЮЛТип import АдрРФЕГРЮЛТип
from .models_.СвАдресЮЛ import СвАдресЮЛ
from .models_.СвНаимЮЛ import СвНаимЮЛ
from .models_.ИдОтпр import ИдОтпр
from .models_.ФИОТип import ФИОТип


class RegionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'КодРегион', 'Регион',)


class ModeEducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'КодСпОбрЮЛ', 'НаимСпОбрЮЛ',)


class FilterBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sortBy', 'label', 'i_d', 'isFilter', 'fields',)


class FilterFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sortBy', 'label', 'i_d', 'asPlaceholder', 'type', 'isFilter',)


class ГРНДатаТипAdmin(admin.ModelAdmin):
    list_display = ('ГРН', 'ДатаЗаписи',)


class АдрРФЕГРЮЛТипAdmin(admin.ModelAdmin):
    list_display = ('Индекс', 'КодРегион', 'КодАдрКладр', 'Дом', 'Корпус', 'Кварт',)


class СвАдресЮЛAdmin(admin.ModelAdmin):
    list_display = ('АдресРФ',)


class СвНаимЮЛAdmin(admin.ModelAdmin):
    list_display = ('НаимЮЛПолн', 'НаимЮЛСокр', 'ГРНДата', 'ГРНДатаИспр',)


class СвЮЛAdmin(admin.ModelAdmin):
    list_display = ('ДатаВып', 'ОГРН', 'ДатаОГРН', 'ИНН', 'КПП', 'СпрОПФ', 'КодОПФ', 'ПолнНаимОПФ', 'СвНаимЮЛ', 'СвАдресЮЛ', )
    # list_display = ('ДатаВып', 'ОГРН',)
    ordering = ['ДатаВып']


class ФайлAdmin(admin.ModelAdmin):
    list_display = ('ИдФайл', 'ВерсФорм', 'ТипИнф', 'ВерсПрог', 'КолДок', 'ИдОтпр',)


class ДокументAdmin(admin.ModelAdmin):
    list_display = ('ИдДок', 'СвЮЛ', 'СвЮЛ_XML', 'Файл', )


class ИдОтпрAdmin(admin.ModelAdmin):
    list_display = ('ДолжОтв', 'Тлф', 'email', 'ФИООтв', )


class ФИОТипAdmin(admin.ModelAdmin):
    list_display = ('Фамилия', 'Имя', 'Отчество',)


admin.site.register(ГРНДатаТип, ГРНДатаТипAdmin)
admin.site.register(АдрРФЕГРЮЛТип, АдрРФЕГРЮЛТипAdmin)
admin.site.register(СвАдресЮЛ, СвАдресЮЛAdmin)
admin.site.register(СвНаимЮЛ, СвНаимЮЛAdmin)
admin.site.register(СвЮЛ, СвЮЛAdmin)
admin.site.register(Файл, ФайлAdmin)
admin.site.register(Документ, ДокументAdmin)
admin.site.register(ИдОтпр, ИдОтпрAdmin)
admin.site.register(ФИОТип, ФИОТипAdmin)
admin.site.register(Regions, RegionsAdmin)
admin.site.register(ModeEducation, ModeEducationAdmin)
admin.site.register(FilterField, FilterFieldAdmin)
admin.site.register(FilterBlock, FilterBlockAdmin)



