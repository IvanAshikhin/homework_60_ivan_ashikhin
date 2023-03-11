from django.urls import path
from webapp.views.base import index_view

from webapp.views.products import detail_view, add_view, update_view, delete_view, confirm_delete

urlpatterns = [
    path("", index_view, name="index_page"),
    path('products/<int:pk>', detail_view, name='details'),
    path('products/add/', add_view, name="add_product"),
    path('products/<int:pk>/update', update_view, name='product_update'),
    path('products/<int:pk>/delete', delete_view, name='delete_product'),
    path('products/<int:pk>/confirm_delete', confirm_delete, name='confirm_delete')
]
