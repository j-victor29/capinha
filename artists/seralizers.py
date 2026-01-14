from rest_framework import serializers
from .models import Artista, ContaBancariaArtista

class ContaBancariaArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContaBancariaArtista
        fields = '__all__'
        read_only_fields = ('artista',)

class ArtistaSerializer(serializers.ModelSerializer):
    conta_bancaria = ContaBancariaArtistaSerializer(read_only=True)

    class Meta:
        model = Artista
        fields = [
            'id',
            'usuario',
            'nome_artistico',
            'biografia',
            'instagram',
            'portfolio_url',
            'ativo',
            'conta_bancaria',
            'criado_em',
            'atualizado_em'
        ]
        read_only_fields = ('usuario',)
