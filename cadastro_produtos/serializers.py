from rest_framework import serializers

from .models import Categoria, Endereco, Fornecedor, PrecoFornecedor, Produto, Telefone


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"


class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = "__all__"


class FornecedorSerializer(serializers.ModelSerializer):
    telefones = serializers.SerializerMethodField(read_only=True)
    enderecos = serializers.SerializerMethodField(read_only=True)

    def get_telefones(self, obj):
        serializer = TelefoneSerializer(obj.telefones.all(), many=True)
        return serializer.data

    def get_enderecos(self, obj):
        serializer = EnderecoSerializer(obj.enderecos.all(), many=True)
        return serializer.data

    class Meta:
        model = Fornecedor
        fields = [
            "id",
            "nome_fantasia",
            "razao_social",
            "cnpj",
            "enderecos",
            "telefones",
        ]


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"


class PrecoFornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrecoFornecedor
        fields = "__all__"
