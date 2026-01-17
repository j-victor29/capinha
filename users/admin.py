from django.contrib import admin
from .models import user, userTelefone, Tipouser


@admin.register(Tipouser)
class TipouserAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']


@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'status', 'data_cadastro', 'tipo_usuario']
    list_filter = ['status', 'data_cadastro', 'tipo_usuario']
    search_fields = ['nome', 'email']
    readonly_fields = ['data_cadastro']
    
    fieldsets = (
        ('Informações Básicas', {'fields': ('nome', 'email', 'status')}),
        ('Tipo de Usuário', {'fields': ('tipo_usuario',)}),
        ('Data', {'fields': ('data_cadastro',)}),
    )


@admin.register(userTelefone)
class UserTelefoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'numero_telefone', 'tipo_telefone']
    list_filter = ['tipo_telefone', 'usuario']
    search_fields = ['usuario__nome', 'numero_telefone']
    
    fieldsets = (
        ('Informações', {'fields': ('usuario', 'numero_telefone', 'tipo_telefone')}),
    )
