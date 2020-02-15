from django.urls import include, path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from . import views

urlpatterns = [
    path("", views.signup_view, name="signup"),
    ]