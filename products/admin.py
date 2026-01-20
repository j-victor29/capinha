from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco_base', 'estoque', 'disponibilidade', 'ativo', 'data_criacao')
    list_filter = ('categoria', 'ativo', 'data_criacao', 'data_atualizacao')
    search_fields = ('nome', 'descricao')
    readonly_fields = ('data_criacao', 'data_atualizacao')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'descricao', 'imagem', 'categoria')
        }),
        ('Preço e Estoque', {
            'fields': ('preco_base', 'estoque')
        }),
        ('Status', {
            'fields': ('ativo',)
        }),
        ('Datas', {
            'fields': ('data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )

    def disponibilidade(self, obj):
        if obj.estoque > 0:
            return f'✅ {obj.estoque} em estoque'
        return '❌ Fora de estoque'
    disponibilidade.short_description = 'Disponibilidade'

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Edição
            return self.readonly_fields + ('data_criacao',)
        return self.readonly_fields
