from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Categoria, Fornecedor
from .serializers import CategoriaSerializer, FornecedorSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    print(queryset)
    serializer_class = CategoriaSerializer


class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
