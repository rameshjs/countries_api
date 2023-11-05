from django.urls import path
from . import views

urlpatterns = [
    path("all", views.country_list, name="country_list"),
    path("<str:common_name>", views.country, name="country"),
]
