from django.urls import path
from .. import views

urlpatterns = [
    path('', views.customer, name='customer'),
    path('show_all/', views.show_customers, name='show_customers'),
    path('create_customer/', views.create_customer, name='create_customer'),
    path('show_customer_products/<int:customer_id>/', views.show_customer_products,
         name='show_customer_products'),
    path('delete_customers/', views.delete_customers, name='delete_customers'),
]
