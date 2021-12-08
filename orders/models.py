from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from localflavor.br.models import BRPostalCodeField, BRStateField
from model_utils.models import TimeStampedModel

from foods.models import Product
from users.models import User


class Order(TimeStampedModel):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    name = models.CharField("Nome no Pedido", max_length=100)
    postal_code = BRPostalCodeField("CEP")
    address = models.CharField("Endereço", max_length=100)
    number = models.CharField("Número", max_length=5)
    complement = models.CharField("Complemento", max_length=100, blank=True)
    district = models.CharField("Bairro", max_length=100)
    state = BRStateField("Estado")
    city = models.CharField("Cidade", max_length=100)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"Pedido {self.id}"


class Item(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(
        validators= [
            MinValueValidator(1),
            MaxValueValidator(20),
        ]
    )

    def __str__(self):
        return str(self.id)
