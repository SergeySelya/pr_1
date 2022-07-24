from django.shortcuts import render
from .models import Task


def about(request):
    tasks = Task.objects.all()
    return render(request, 'about.html', {'tasks':tasks})


def main(request):
    return render(request, 'main.html')
