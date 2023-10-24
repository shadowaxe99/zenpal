
from django.urls import path
from . import views

app_name = 'interaction_tracking'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_interaction, name='add_interaction'),
    path('edit/<int:interaction_id>/', views.edit_interaction, name='edit_interaction'),
    path('delete/<int:interaction_id>/', views.delete_interaction, name='delete_interaction'),
]
