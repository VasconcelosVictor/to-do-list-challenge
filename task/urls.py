from django.urls import path
from .views import *

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', TaskListView.as_view(), name='task-list'),
    path('tasks/add/', TaskCreateView.as_view(), name='task-add'),
    path('tasks/edit/<int:pk>/',TaskUpdateView.as_view(), name='task-edit'),
    path('tasks/delete/<int:task_id>/', DeleteTaskView.as_view(), name='delete_task'),
    path('task/change/status/<int:task_id>', ChangeStatusView.as_view(), name='change-status'),

    # Times 
    path('times/', TimeListView.as_view(), name='times-list'),
    path('times/<int:task_id>/', CreateTimeRecord.as_view(), name='time-add'),
    path('time/delete/<int:record_id>/', DeleteRecordView.as_view(), name='delete_record'),
]