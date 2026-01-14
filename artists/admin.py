from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Artista, ContaBancariaArtista

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_artistico', 'ativo')
    search_fields = ('nome_artistico',)
    list_filter = ('ativo',)


@admin.register(ContaBancariaArtista)
class ContaBancariaArtistaAdmin(admin.ModelAdmin):
    list_display = ('artista', 'banco', 'tipo_conta')
