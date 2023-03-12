from django.db import models

from webapp.models.product import Product


class ProductCart(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.PROTECT,
                                verbose_name='Продукт в корзине')
    count = models.IntegerField(null=False, verbose_name='Количество', default=0)
