from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.todos, name='todos'),
    path('add', views.addTodos, name='add'),
    path('complete/<int:todo_id>', views.completeTodo, name='complete'),
    path('delete/<int:todo_id>', views.deleteTodo, name='delete'),
    path('undo/<int:todo_id>', views.undoTodo, name='undo'),
]