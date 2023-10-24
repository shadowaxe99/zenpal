
from django.urls import path
from . import views

app_name = 'email_integration'

urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.send_email, name='send_email'),
    path('inbox/', views.view_inbox, name='view_inbox'),
]
