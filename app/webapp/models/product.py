from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=1000, null=False, blank=False, verbose_name='Название продукта')
    description = models.TextField(max_length=10000, null=True, verbose_name='Описание')
    image = models.TextField(max_length=10000, null=False, blank=False, verbose_name='Ссылка изображения')
    category = models.TextField(max_length=500, null=False, blank=False, verbose_name='Категория', default='Other')
    remain = models.IntegerField(null=False, verbose_name='Остаток', validators=[MinValueValidator(0)])
    cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
