from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def about(request):
    tasks = Task.objects.all()
    return render(request, 'about.html', {'tasks':tasks})


def main(request):
    return render(request, 'main.html')


def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'форма была не верной'

    form = TaskForm()
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'create.html', context)
