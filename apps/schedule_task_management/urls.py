
from django.urls import path
from . import views

app_name = 'schedule_task_management'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_task, name='create_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
