from rest_framework import serializers
from .models import Impressora


class ImpressoraListSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Impressora
        fields = ['id', 'nome', 'tipo', 'tipo_display', 'status', 'status_display', 'localizacao', 'data_criacao']
        read_only_fields = ['id', 'data_criacao']


class ImpressoraDetailSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Impressora
        fields = ['id', 'nome', 'tipo', 'tipo_display', 'status', 'status_display', 'localizacao', 
                  'fabricante', 'modelo', 'data_aquisicao', 'data_ultima_manutencao', 'data_criacao']
        read_only_fields = ['id', 'data_criacao']


class ImpressoraCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impressora
        fields = ['nome', 'tipo', 'status', 'localizacao', 'fabricante', 'modelo', 'data_aquisicao', 'data_ultima_manutencao']