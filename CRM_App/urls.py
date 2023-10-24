
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact_management/', include('apps.contact_management.urls')),
    path('interaction_tracking/', include('apps.interaction_tracking.urls')),
    path('schedule_task_management/', include('apps.schedule_task_management.urls')),
    path('email_integration/', include('apps.email_integration.urls')),
]
