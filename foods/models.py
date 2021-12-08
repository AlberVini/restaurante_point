from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from users.models import Restaurant


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(disponivel=True)


class Category(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome")

    class Meta:
        ordering = ("nome",)
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("products:lists_by_category", kwargs={"slug": self.slug})


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=255, null=False, blank=False)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome")
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    imagem = models.ImageField(upload_to="produtos/%Y/%m/%d", blank=True)
    restaurante = models.ForeignKey(Restaurant, null=False, blank=False, on_delete=models.CASCADE, related_name="restaurante")
    disponivel = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("nome",)
        verbose_name = "produto"
        verbose_name_plural = "produtos"

    def __str__(self) -> str:
        return self.nome
    
    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})
