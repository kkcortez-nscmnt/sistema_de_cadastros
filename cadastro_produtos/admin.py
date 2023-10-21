from django.contrib import admin

from .models import Categoria, Fornecedor, PrecoFornecedor, Produto

admin.site.register(Categoria)
admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(PrecoFornecedor)
