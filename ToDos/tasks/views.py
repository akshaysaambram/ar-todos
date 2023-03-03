from .models import Task, User
from .forms import TaskForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'tasks/home.html')

@login_required
def tasks(request):

    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
        return redirect("tasks")

    context = {
        'form' : form,
    }

    return render(request, 'tasks/tasks.html', context)

@login_required
def update(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()          
        return redirect("tasks")

    context = {
        'form' : form,
    }

    return render(request, 'tasks/update_task.html', context)

@login_required
def delete(request, pk):
    task = Task.objects.get(id=pk) 

    form = TaskForm(instance=task)
    if request.method == "POST":
        task.delete()
        return redirect("tasks")
    context = {
        'task' : task,
    }

    return render(request, 'tasks/delete_task.html', context)
