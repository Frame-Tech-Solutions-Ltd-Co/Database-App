from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('verify/', views.verify, name='verify'),
]
