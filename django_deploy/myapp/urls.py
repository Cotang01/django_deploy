from django.urls import path, include
from . import views
from .ext_urls import customer_urls, product_urls, order_urls

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', include(customer_urls)),
    path('product/', include(product_urls)),
    path('order/', include(order_urls))
]

