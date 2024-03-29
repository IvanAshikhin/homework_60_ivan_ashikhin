# Generated by Django 4.1.7 on 2023-03-12 13:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_order_productquantity_order_quantities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantities',
            field=models.ManyToManyField(related_name='orders_quantities', through='webapp.ProductQuantity', to='webapp.product', verbose_name='Quantities'),
        ),
        migrations.AlterField(
            model_name='productquantity',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.order', verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='productquantity',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.product', verbose_name='Good'),
        ),
        migrations.AlterField(
            model_name='productquantity',
            name='quantity',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantity'),
        ),
    ]
