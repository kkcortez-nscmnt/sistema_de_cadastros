from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CategoriaViewSet, FornecedorViewSet, home

router = DefaultRouter()
router.register("categorias", CategoriaViewSet, basename="categoria")
router.register("fornecedores", FornecedorViewSet, basename="fornecedor")

urlpatterns = [path("", home, name="home")]
