# pixelate/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.pixelate_view, name="pixelate"),
]
