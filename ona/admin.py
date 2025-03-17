from django.contrib import admin
from .models import Departs, Employee, EmailTalks
# Register your models here.

admin.site.register(Departs)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'depart', 'idade', 'level', 'genero', 'salario')
    search_fields = ('nome', 'depart__nome', 'cidade')
    list_filter = ('depart', 'genero', 'tipo_colaborador')
    ordering = ('nome',)

# Personalizando a exibição do EmailTalks
@admin.register(EmailTalks)
class EmailTalksAdmin(admin.ModelAdmin):
    list_display = ('remetente', 'destinatario', 'data_envio', 'hash_id', 'origem')
    search_fields = ('remetente__nome', 'destinatario__nome')
    list_filter = ('data_envio',)
    ordering = ('-data_envio',)