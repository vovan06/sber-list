from django.urls import path

from .views import (
    MainTaskAPIView, MainTaskDetailAPIView,

    TaskStatusAPIView, TaskStatusDetailAPIView,
    
    SubTaskAPIView, SubTaskDetailAPIView,

    MainTaskForUserAPIView, SubTaskForUserAPIView
)

urlpatterns = [
    path('task/main/', MainTaskAPIView.as_view(), name='task_list'),
    path('task/main/<uuid:pk>/', MainTaskDetailAPIView.as_view(), name='task_detail'),
    path('task/main/by/user/<uuid:pk>/', MainTaskForUserAPIView.as_view(), name='subtask_list_by_user'),


    path('status/', TaskStatusAPIView.as_view(), name='status_list'),
    path('status/<int:pk>/', TaskStatusDetailAPIView.as_view(), name='status_detail'),

    path('subtasks/', SubTaskAPIView.as_view(), name='sub_task_list'),
    path('subtasks/<uuid:pk>/', SubTaskDetailAPIView.as_view(), name='sub_task_detail'),
    path('subtasks/by/user/<uuid:pk>/', SubTaskForUserAPIView.as_view(), name='subtask_list_by_user'),

]
