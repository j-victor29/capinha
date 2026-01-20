from rest_framework import serializers
from .models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    categoria_display = serializers.CharField(source='get_categoria_display', read_only=True)
    disponivel = serializers.SerializerMethodField()

    class Meta:
        model = Produto
        fields = [
            'id', 'nome', 'descricao', 'categoria', 'categoria_display',
            'preco_base', 'estoque', 'disponivel', 'ativo', 'data_criacao', 'data_atualizacao'
        ]
        read_only_fields = ['data_criacao', 'data_atualizacao']

    def get_disponivel(self, obj):
        return obj.estoque > 0