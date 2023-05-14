from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.record_details, name='record_details'),
    path('api-access/', views.record_api_access, name='record_api_access'),
]
