from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [

    path('basket/', views.basket, name='basket'),
    path('basket/<int:product_id>/', views.delete, name='delete'),
    path('', views.home, name='home'),
]
