from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import TodoList
from .forms import TodoListForm

def index(request):
    todos = TodoList.objects.all()
    return render(request, 'todo_app/index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoListForm()
    return render(request, 'todo_app/add_todo.html', {'form': form})

def delete_todo(request, todo_id):
    todo = get_object_or_404(TodoList, id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    return render(request, 'todo_app/delete_todo.html', {'todo': todo})

def get_events(request):
    todos = TodoList.objects.all()
    events = []
    for todo in todos:
        if todo.due_date:
            events.append({
                'title': todo.title,
                'start': todo.due_date.strftime('%Y-%m-%dT%H:%M:%S'),
            })
    return JsonResponse(events, safe=False)

