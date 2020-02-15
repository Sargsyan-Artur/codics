from django.urls import include, path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from . import views#, HomePageView

app_name = 'home'

urlpatterns = [

    path('basket/', views.basket, name='basket'),
    path('basket/<int:product_id>/', views.delete, name='delete'),
    path('', views.home, name='home'),

   # path('', HomePageView.as_view(), name='home'),

    ]