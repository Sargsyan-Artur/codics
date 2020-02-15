from django.shortcuts import render, get_object_or_404
from employees.models import Products, Basket
from django.shortcuts import redirect


def home(request):
    if request.method == 'POST':

        product = get_object_or_404(Products, id=request.POST['product'])
        basket = Basket.objects.get_or_create(user=request.user)
        basket.products.add(product)
        basket.save()

    products = Products.objects.all()
    return render(request, 'home.html', {'products': products})


def basket(request):
    user = request.user

    products = Products.objects.filter(basket__user=user)
    return render(request, 'basket_products.html', {'products': products})


def delete(request, product_id):
    basket = Basket.objects.get(user=request.user)
    basket.products.remove(product_id)
    return redirect('/home/basket/')
