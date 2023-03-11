from django.contrib import admin

from webapp.models import Product


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'description', 'image', 'category', 'remain', 'cost')
    list_filter = ('id', 'product_name', 'description', 'image', 'category', 'remain', 'cost')
    search_fields = ('id', 'product_name', 'category')
    fields = ('product_name', 'category', 'cost', 'description')
    readonly_fields = ('id', 'image')


admin.site.register(Product, ProductAdmin)