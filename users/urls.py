from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.signup_view, name="signup"),
 ]