from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.urls import reverse_lazy
from employees.models import Products, Basket
from .forms import ProductsForm, BasketForm
from django.http import HttpResponse
from django.contrib.auth.models import User


# class HomePageView(ListView):
#     model = Products
#     form_class = ProductsForm
#     template_name = 'home.html'
#     success_url = reverse_lazy('home')
#     products = Products.objects.all()
#     print(products)
#     print('HomePageView')


# def home(request):
#     basket = BasketForm(request.POST)
#     products = Products.objects.all()
#
#     return render(
#         request, 'home.html', {'products': products, 'basket_form': basket}
#     )

def home(request):
    if request.method == 'POST':
       # basket = BasketForm(request.POST)

        print(request.POST)
        print(request.user)
        print(request.POST['product'])
        product = get_object_or_404(Products, id=request.POST['product'])
        basket = Basket.objects.create(user=request.user, products=product)
        basket.save()
        print(product)
        print(basket)
        print('start if if if')
        #if basket.is_valid():
            # process the data in form.cleaned_data as required
            #p = basket.save()
            #print("ifffffffff")
    products = Products.objects.all()
    print('home')
    return render(request, 'home.html', {'products': products})

    # def get_queryset(self):
    #     return Products.objects.filter(user_id=self.request.user.id)


def basket(request):
    products = Products.objects.all()
    user = request.user
    basket = Basket.objects.filter(user=user)
    context = []
    for user_basket in basket:
        print(user_basket.products.id)

        a = get_object_or_404(Products, id=user_basket.products.id)
        print(type(a))
        print(a.name)
        context += [a]

    return render(request, 'basket_products.html', {'context': context, 'products': products})


# def basket(request):
#     products = Products.objects.all()
#     # print(type(products))
#
#     user = request.user
#     user_basket = user.basket_set.all()
#     basket = Basket.objects.filter(user=user)
#     print(basket)
#
#     print('----------')
#     # for i in basket:
#     #     print(i)
#     # print(basket)
#     context = Basket.objects.filter(user=user).select_related('products')
#
#     context = []
#     for i in basket:
#         print(i.products.id)
#
#         a = Products.objects.get(id=i.products.id)
#         print(type(a))
#         print(a.name)
#         context +=[a]
#         #print(i.select_related('products'))
#
#     print(context)
#
#
#     return render(request, 'basket_products.html', {'context': context, 'products': products})





# def basket(request):
#
#     user = request.user
#     products = Products.objects.all()
#     user_basket = user.basket_set.all()
#
#     print(user_basket)
#     for each_prod in user_basket:
#         print(each_prod.products.id)
#
#         #basket += [Products.objects.filter(id=each_prod.products.id)]
#         #baskets = Products.objects.values(each_prod)
#
#     # for i in basket:
#     #     print(i)
#     #     print(type(i))
#
#     return render(request, 'basket_products.html', {'user_basket': user_basket})


def delete(request, product_id):
    user = request.user
    basket = get_object_or_404(Basket, user=user, id=product_id)
    print('dddddddddddddddddddddddd')
    print(basket)
    return HttpResponse('asdddddd')
