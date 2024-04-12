from django.db import models
from random import randint


class Customer(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.PositiveIntegerField(blank=False, null=False)
    address = models.CharField(max_length=50, blank=True, null=True)
    registration_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.pk} - {self.name} - {self.email}'


class Product(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    desc = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=False, null=False)
    quantity = models.PositiveIntegerField(blank=False, null=False)
    publish_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='',
                              default=f'image{randint(0, 1_000_000)}.png')

    def __str__(self):
        return f'{self.name} - {self.price}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.FloatField(blank=False, null=False)
    creation_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.pk} - {self.customer} - ' \
               f'Товары: {self.products} - {self.creation_date} - ' \
               f'Стоимость заказа: {self.total_price}'

