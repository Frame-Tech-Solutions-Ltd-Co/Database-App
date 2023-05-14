from django.urls import path
from . import views

urlpatterns = [
    path('records/', views.database_records, name='database_records'),
    path('search/', views.search_filter, name='search_filter'),
]