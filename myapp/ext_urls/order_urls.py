from django.urls import path
from .. import views

urlpatterns = [
    path('', views.order, name='order'),
    path('show_all/', views.show_orders, name='show_orders'),
    path('create_order/', views.create_order, name='create_order'),
    path('delete_orders/', views.delete_orders, name='delete_orders'),
]
