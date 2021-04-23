from django.urls import path
from . import views

urlpatterns = [
    path('', views.work_home, name='work_home'),
    path('/create',views.create, name='create'),
    path('/<int:pk>/update', views.TaskUpdateView.as_view(), name='task-update'),
    path('/<int:pk>/delete', views.TaskDeleteView.as_view(), name='task-delete'),
    path('/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
]
