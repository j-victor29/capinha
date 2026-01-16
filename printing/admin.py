from django.contrib import admin
from .models import Impressora


@admin.register(Impressora)
class ImpressoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'status', 'localizacao', 'fabricante', 'data_criacao')
    list_filter = ('tipo', 'status', 'data_criacao')
    search_fields = ('nome', 'fabricante', 'modelo', 'localizacao')
    readonly_fields = ('data_criacao',)
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'tipo', 'status')
        }),
        ('Especificações', {
            'fields': ('fabricante', 'modelo', 'localizacao')
        }),
        ('Datas', {
            'fields': ('data_aquisicao', 'data_ultima_manutencao', 'data_criacao')
        }),
    )