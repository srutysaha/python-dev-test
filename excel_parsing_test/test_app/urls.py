from django.urls import path
from .views import product_list, upload_products

urlpatterns = [
    path('', product_list, name='product_list'),
    path('upload/', upload_products, name='upload_products'),
]
