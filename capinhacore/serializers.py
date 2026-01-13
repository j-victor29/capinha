from rest_framework import serializers
from .models import (
    TipoUsuario, Usuario, UsuarioTelefone,
    Recompensa, UsuarioRecompensa, ContaBancaria
)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class UsuarioTelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioTelefone
        fields = '__all__'


class RecompensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recompensa
        fields = '__all__'


class UsuarioRecompensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRecompensa
        fields = '__all__'


class ContaBancariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContaBancaria
        fields = '__all__'