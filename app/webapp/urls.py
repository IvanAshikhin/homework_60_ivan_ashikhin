from django.urls import path
from webapp.views.base import IndexView
from webapp.views.products import ProductDetail
from webapp.views.products import ProductAddView, ProductUpdateView, ProductDeleteView
from webapp.views.cart import AddToCartView
from webapp.views.cart import CartView
from webapp.views.cart import DeleteCartView

urlpatterns = [
    path("", IndexView.as_view(), name="index_page"),
    path('products/<int:pk>', ProductDetail.as_view(), name='details'),
    path('products/add/', ProductAddView.as_view(), name="add_product"),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='delete_product'),
    path('add_to_cart/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/remove/<int:pk>/', DeleteCartView.as_view(), name='delete_cart'),

]
