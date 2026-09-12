from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all().order_by('-created')
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('/')
    return render(request, 'tasks/list.html', {'tasks': tasks})

def toggle_task(request, pk):
    task = Task.objects.get(id=pk)
    task.complete = not task.complete
    task.save()
    return redirect('/')

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')