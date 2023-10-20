from django.db import models


class Categoria(models.Model):
    """Model definition for Categoria."""

    nome = models.CharField(max_length=200, unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Categoria."""

        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        """Unicode representation of Categoria."""
        return self.nome


class Fornecedor(models.Model):
    """Model definition for Fornecedor."""

    nome_fantasia = models.CharField(max_length=200)
    razao_social = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, unique=True)
    telefones = models.CharField(max_length=200)

    class Meta:
        """Meta definition for Fornecedor."""

        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        """Unicode representation of Fornecedor."""
        return f"{self.nome_fantasia}"


class Produto(models.Model):
    """Model definition for Produto."""

    nome = models.CharField(max_length=200)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fornecedores = models.ManyToManyField(
        "Fornecedor", related_name="produtos", through="PrecoFornecedor"
    )

    class Meta:
        """Meta definition for Produto."""

        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        """Unicode representation of Produto."""
        return self.nome


class PrecoFornecedor(models.Model):
    """Model definition for PrecoFornecedor."""

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """Meta definition for PrecoFornecedor."""

        unique_together = ("produto", "fornecedor")
        verbose_name = "PrecoFornecedor"
        verbose_name_plural = "PrecoFornecedores"

    def __str__(self):
        """Unicode representation of PrecoFornecedor."""
        return f"Preço de {self.produto.nome} fornecido por {self.fornecedor.nome_fantasia}"
