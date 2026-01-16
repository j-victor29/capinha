from rest_framework import serializers
from .models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'telefone', 'cidade', 'data_criacao']
        read_only_fields = ['id', 'data_criacao']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'telefone', 'endereco', 'cidade', 'estado', 'cep', 'data_criacao', 'is_active']
        read_only_fields = ['id', 'data_criacao']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'telefone', 'endereco', 'cidade', 'estado', 'cep']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user