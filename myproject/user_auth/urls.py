from django.urls import path
import views

app_name = 'user_auth'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('verify/', views.verify, name='verify'),
]
