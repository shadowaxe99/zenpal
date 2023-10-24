
from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'schedule_task_management/index.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        task = Task()
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.save()
        return redirect('schedule_task_management:index')
    else:
        return render(request, 'schedule_task_management/create_task.html')

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.save()
        return redirect('schedule_task_management:index')
    else:
        return render(request, 'schedule_task_management/update_task.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('schedule_task_management:index')
