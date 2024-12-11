from django.urls import path
from . import views

# Это пути 
urlpatterns = [
    path('', views.index, name='index'),
    path('todo_list', views.todo_list, name='todo_list')
]

