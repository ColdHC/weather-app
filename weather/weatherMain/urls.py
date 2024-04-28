from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import WeatherMainView

urlpatterns = [
    path('', WeatherMainView.as_view(), name='weather_main'),
]
