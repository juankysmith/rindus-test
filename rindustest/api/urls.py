from django.urls import path

from . import views

urlpatterns = [
    path("", views.loadinitialdata, name="initial_load"),
]