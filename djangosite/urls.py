"""djangosite URL configuration."""

from django.contrib import admin
from django.urls import path

from demo import views

urlpatterns = [
    path("", views.index, name="index"),
    path("health/", views.health, name="health"),
    path("admin/", admin.site.urls),
]
