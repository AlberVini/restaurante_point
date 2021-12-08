from django.contrib.auth.models import AbstractUser
from django.db import models
from localflavor.br.models import BRCNPJField


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='client')
    endereco = models.CharField(max_length=255, null=True)
    data_nascimento = models.DateField(null=True)
    celular = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self) -> str:
        return str(self.user)


class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='restaurant')
    nome = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    cnpj = BRCNPJField()
    imagem = models.ImageField(upload_to="restaurant/%Y/%m/%d", null=True, blank=True)

    def __str__(self) -> str:
        return str(self.user)
