from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Employee(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, blank=True, help_text='Contact phone number')
    mail = models.EmailField(max_length=254)
    address = models.CharField(max_length=200)
    salary = models.CharField(max_length=50)

    POSITION = (
        ('a', 'accountant'),
        ('m', 'manager'),
        ('s', 'seller'),
        ('sa', 'sales assistant'),
    )
    position = models.CharField(max_length=4, choices=POSITION, blank=True, default='s', help_text='v')

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=200)
    images = models.ImageField(upload_to="images/", null=True, blank=True)
    price = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    count = models.IntegerField()

    TYPE = (
        ('c', 'computers'),
        ('l', 'laptops'),
        ('p', 'phones'),
        ('tv', 'TV'),
    )

    type = models.CharField(max_length=4, choices=TYPE, blank=True, default='', help_text='v')

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, through='BasketProducts')

    def __str__(self):
        return self.user.username


class BasketProducts(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)

