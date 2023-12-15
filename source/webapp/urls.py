from django.urls import path
from .views import index_view, task_create_view, task_view, task_delete_view, task_update_view

urlpatterns = [
    path('', index_view, name='index'),
    path('articles/add/', task_create_view, name='task-create'),
    path('article/<int:pk>/', task_view, name='task-detail'),
    path('article/<int:pk>/update/', task_update_view.as_view(), name='task_update_view'),
    path('article/<int:pk>/delete/', task_delete_view.as_view(), name='task_delete_view'),
]
