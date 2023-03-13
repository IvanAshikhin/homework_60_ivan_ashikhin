from django.db import models
from django.core.validators import MinValueValidator
from webapp.models import Product


class Order(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    phone = models.CharField(max_length=20, null=False, blank=False, verbose_name='Number')
    address = models.CharField(max_length=500, null=False, blank=False, verbose_name='Address')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Date')
    items = models.ManyToManyField(Product, through='OrderItem')


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
