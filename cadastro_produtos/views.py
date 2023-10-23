import requests
from django.shortcuts import render
from rest_framework import viewsets

from .models import Categoria, Fornecedor
from .serializers import CategoriaSerializer, FornecedorSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
