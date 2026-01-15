from rest_framework import viewsets
from .models import Printer, PrintQueue
from .serializers import PrinterSerializer, PrintQueueSerializer

class PrinterViewSet(viewsets.ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer

class PrintQueueViewSet(viewsets.ModelViewSet):
    queryset = PrintQueue.objects.all()
    serializer_class = PrintQueueSerializer