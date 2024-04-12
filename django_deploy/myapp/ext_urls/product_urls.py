from django.urls import path
from .. import views

urlpatterns = [
    path('', views.product, name='product'),
    path('show_all/', views.show_products, name='show_products'),
    path('create_product/', views.create_product, name='create_product'),
    path('delete_product/', views.delete_products, name='delete_products'),
]
