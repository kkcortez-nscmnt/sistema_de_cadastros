from rest_framework import serializers

from .models import Categoria, Fornecedor, PrecoFornecedor, Produto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = "__all__"


class PrecoFornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrecoFornecedor
        fields = "__all__"


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
