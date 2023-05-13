from django.urls import path
from . import views

app_name = 'credit_system'

urlpatterns = [
    path('purchase/', views.purchase_credits, name='purchase_credits'),
]
