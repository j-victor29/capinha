from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Impressora
from .serializers import ImpressoraListSerializer, ImpressoraDetailSerializer, ImpressoraCreateUpdateSerializer

class ImpressoraViewSet(viewsets.ModelViewSet):
    queryset = Impressora.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return ImpressoraCreateUpdateSerializer
        elif self.action == 'retrieve':
            return ImpressoraDetailSerializer
        return ImpressoraListSerializer
    
    @action(detail=False, methods=['get'])
    def ativas(self, request):
        """Retorna apenas impressoras ativas"""
        impressoras = self.queryset.filter(status='ativo')
        serializer = ImpressoraListSerializer(impressoras, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def marcar_manutencao(self, request):
        """Marca impressora como em manutenção"""
        impressora = self.get_object()
        impressora.status = 'manutencao'
        impressora.save()
        serializer = ImpressoraDetailSerializer(impressora)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def ativar(self, request):
        """Ativa impressora"""
        impressora = self.get_object()
        impressora.status = 'ativo'
        impressora.save()
        serializer = ImpressoraDetailSerializer(impressora)
        return Response(serializer.data)