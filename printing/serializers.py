from rest_framework import serializers
from .models import Printer, PrintQueue

class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = '__all__'

class PrintQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintQueue
        fields = '__all__'