from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_profile, name='user_profile'),
    path('company/', views.company_profile, name='company_profile'),
]
