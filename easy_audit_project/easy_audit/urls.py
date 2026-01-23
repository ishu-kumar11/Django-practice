from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('history/<int:pk>/', views.task_history, name='task_history'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]
