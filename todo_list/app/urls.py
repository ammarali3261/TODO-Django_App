from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, TaskReorder, Signup
from django.contrib.auth.views import LogoutView


urlpatterns = [
     path('task-list-api/', views.TaskListAPI, name='task-list-api'),
     path('task-detail-api/<str:pk>/', views.TaskDetailAPI, name='task-detail-api'),
     path('task-update-api/<str:pk>/', views.TaskUpdateAPI, name='task-update-api'),
     path('task-create-api/', views.TaskCreateAPI, name='task-create-api'),
     path('task-delete-api/<str:pk>/', views.TaskDeleteAPI, name='task-delete-api'),
     
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', Signup.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('update-task<int:pk>/', TaskUpdate.as_view(), name='update-task'),
    path('delete-task<int:pk>/', TaskDelete.as_view(), name='delete-task'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
]