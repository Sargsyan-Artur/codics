from django import forms
from employees.models import Products, Basket


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'images', 'price']


class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = '__all__'
