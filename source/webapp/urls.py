from django.urls import path
from .views import index_view, task_create_view, task_view

urlpatterns = [
    path('', index_view, name='index'),
    path('articles/add/', task_create_view, name='task-create'),
    path('article/<int:pk>/', task_view, name='task-detail')
]
