from datetime import timedelta

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from . import forms
from . import models


def index(request):
    return render(request, "index.html")


def customer(request):
    return render(request, "customer_panel.html")


def product(request):
    return render(request, "product_panel.html")


def order(request):
    return render(request, "order_panel.html")


def create_customer(request):
    context = {}
    form = forms.CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "create_customer.html", context)


def show_customers(request):
    context = {"customers": models.Customer.objects.all()}
    return render(request, "customers.html", context)


def delete_customers(request):
    if request.method == 'POST':
        for c_id in request.POST.getlist('customers_to_delete'):
            customer = models.Customer.objects.get(id=c_id)
            customer.delete()
            return HttpResponseRedirect('/customer/')
    return render(request, 'delete_customers.html',
                  {"customers": models.Customer.objects.all()})


def create_product(request):
    context = {}
    form = forms.ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
        image = form.cleaned_data['image']
        fs = FileSystemStorage()
        fs.save(image.name, image)
        form.save()
    context["form"] = form
    return render(request, "create_product.html", context)


def show_products(request):
    context = {"products": models.Product.objects.all()}
    return render(request, "products.html", context)


def delete_products(request):
    if request.method == 'POST':
        for p_id in request.POST.getlist('products_to_delete'):
            product = models.Product.objects.get(id=p_id)
            product.delete()
            return HttpResponseRedirect('/product/')
    return render(request, 'delete_products.html',
                  {"products": models.Product.objects.all()})


def create_order(request):
    context = {}
    if request.method == "POST":
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.OrderForm()
        form.fields["products"].queryset = models.Product.objects.all()
    context["form"] = form
    return render(request, "create_order.html", context)


def show_orders(request):
    context = {"orders": models.Order.objects.all()}
    return render(request, "orders.html", context)


def delete_orders(request):
    if request.method == 'POST':
        for o_id in request.POST.getlist('orders_to_delete'):
            order = models.Order.objects.get(id=o_id)
            order.delete()
            return HttpResponseRedirect('/order/')
    return render(request, 'delete_orders.html',
                  {"orders": models.Order.objects.all()})


def show_customer_products(request, customer_id):
    customer_ = models.Customer.objects.get(id=customer_id)
    time_period = int(request.POST.get('time_period', 7))
    start_date = timezone.now() - timedelta(days=time_period)
    customer_orders = models.Order.objects\
        .filter(customer=customer_, creation_date__gte=start_date)\
        .prefetch_related('products')
    product_list = set()
    for o in customer_orders:
        p_list = o.products.all()
        for p in p_list:
            product_list.add(p)
    context = {'customer': customer_, 'ordered_products': product_list}
    return render(request, 'customer_products.html', context)
