from django.contrib import admin
from .models import Printer, PrintQueue

@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modelo', 'status', 'ativa')
    list_filter = ('status', 'ativa')

@admin.register(PrintQueue)
class PrintQueueAdmin(admin.ModelAdmin):
    list_display = ('pedido_id', 'printer', 'status', 'criado_em')
    list_filter = ('status', 'printer')