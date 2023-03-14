from django.contrib import admin
from webapp.models import Product

from webapp.models import Order
from webapp.models.order import OrderItem


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'description', 'image', 'category', 'remain', 'cost')
    list_filter = ('id', 'product_name', 'description', 'image', 'category', 'remain', 'cost')
    search_fields = ('id', 'product_name', 'category')
    fields = ('product_name', 'category', 'cost', 'description')
    readonly_fields = ('id', 'image')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phone', 'address', 'created_at')
    list_filter = ('id', 'username', 'phone', 'address', 'created_at')
    search_fields = ('id', 'username', 'phone')
    readonly_fields = ['id']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'order', 'quantity')
    list_filter = ('id', 'product', 'order', 'quantity')
    search_fields = ('id', 'product', 'order')
    readonly_fields = ['id']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
