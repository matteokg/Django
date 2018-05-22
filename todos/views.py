from django.shortcuts import render, redirect
from .models import Todos
from .forms import TodoForm
from django.http import HttpResponse

# Create your views here.

def todos(request):
    todo_list = Todos.objects.all()
    
    
    context = {'todo_list': todo_list}
    
    return render(request, 'todos/todoMain.html', context)


def addTodos(request):

    new_todo = Todos(text=request.POST['text'])
    new_todo.save()

    print(new_todo)
    return redirect('todos:todos')
    

def deleteTodo(request, todo_id):
    todo = Todos.objects.get(pk=todo_id)
    todo.delete()
    return redirect('todos:todos')
    
def completeTodo(request, todo_id):
    todo = Todos.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('todos:todos')

def undoTodo(request, todo_id):
    todo = Todos.objects.get(pk=todo_id)
    todo.complete = False
    todo.save()
    return redirect('todos:todos')