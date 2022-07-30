from django.shortcuts import render
from .models import Task
from .forms import TaskForm


def about(request):
    tasks = Task.objects.all()
    return render(request, 'about.html', {'tasks':tasks})


def main(request):
    return render(request, 'main.html')


def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    form = TaskForm()
    context = {
        "form": form
    }
    return render(request, 'create.html', context)
