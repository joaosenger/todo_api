from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodoCreateListView.as_view(), name='todo-create-list-view'),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroyView.as_view(), name='todo-detail-view'),
]
