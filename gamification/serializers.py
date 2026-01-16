from rest_framework import serializers
from .models import Recompensa, UsuarioRecompensa


class RecompensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recompensa
        fields = [
            'id',
            'nome',
            'descricao',
            'tipo',
        ]

class UsuarioRecompensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRecompensa
        fields = [
            'id',
            'usuario',
            'recompensa',
            'data_recompensa',
        ]
        read_only_fields = ['data_recompensa']
