from rest_framework.routers import DefaultRouter

from .views import CategoriaViewSet, FornecedorViewSet

router = DefaultRouter()
router.register("categorias", CategoriaViewSet, basename="categoria")
router.register("fornecedores", FornecedorViewSet, basename="fornecedor")
