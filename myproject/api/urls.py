from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_endpoints, name='api_endpoints'),
]