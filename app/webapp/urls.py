from django.urls import path
from webapp.views.base import IndexView
from webapp.views.products import ProductDetail
from webapp.views.products import TaskAddView
from webapp.views.products import TaskUpdateView
from webapp.views.products import TaskDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name="index_page"),
    path('products/<int:pk>', ProductDetail.as_view(), name='details'),
    path('products/add/', TaskAddView.as_view(), name="add_product"),
    path('products/<int:pk>/update', TaskUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', TaskDeleteView.as_view(), name='delete_product'),

]
