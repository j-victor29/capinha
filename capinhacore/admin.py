from django.contrib import admin
from .models import TipoUsuario, UsuarioTelefone, UsuarioRecompensa, ContaBancaria, Usuario

admin.site.register(TipoUsuario)
admin.site.register(UsuarioTelefone)
admin.site.register(UsuarioRecompensa)
admin.site.register(ContaBancaria)
admin.site.register(Usuario)