from django.urls import path
from . import views

urlpatterns = [
    path('products', views.products_list_mobile, name='products-list-mobile'),
    path('products/<int:pk>', views.product_detail_mobile, name='product-detail-mobile'),
]