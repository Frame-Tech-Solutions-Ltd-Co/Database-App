# added the necessary paths for db_interaction, record_access, alert_system, api, and profiles apps. This ensures that the URLs are properly routed to their respective views.

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_auth/', include('user_auth.urls')),
    path('credit_system/', include('credit_system.urls')),
    path('db_interaction/', include('db_interaction.urls')),
    path('record_access/', include('record_access.urls')),
    path('alert_system/', include('alert_system.urls')),
    path('api/', include('api.urls')),
    path('profiles/', include('profiles.urls')),
]
