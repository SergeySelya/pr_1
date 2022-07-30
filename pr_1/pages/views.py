from django.shortcuts import render
from .models import Task
from .forms import TaskForm


def about(request):
    tasks = Task.objects.all()
    return render(request, 'about.html', {'tasks':tasks})


def main(request):
    return render(request, 'main.html')


def create(request):
    form = TaskForm()
    context = {
        "form": form
    }
    tasks = Task.objects.all()
    return render(request, 'create.html', context)
