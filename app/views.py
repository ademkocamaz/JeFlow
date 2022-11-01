from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Category, Process, Activity, Task

# Create your views here.


@login_required(login_url='/user/login/')
def index(request):
    return render(request, 'app/index.html')


def category(request):
    categories = Category.objects.order_by('-created_date')
    context = {
        'categories': categories
    }
    return render(request, 'app/category.html', context)


def process(request):
    processes = Process.objects.order_by('created_date')
    context = {
        'processes': processes
    }
    return render(request, 'app/process.html', context)


def activity(request):
    activities = Activity.objects.order_by('created_date')
    context = {
        'activities': activities
    }
    return render(request, 'app/activity.html', context)


def task(request):
    tasks = Task.objects.order_by('created_date')
    context = {
        'tasks': tasks
    }
    return render(request, 'app/task.html', context)
