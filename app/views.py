from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Category, Process, Activity, Task
from .forms import CategoryForm, ProcessForm, ActivityForm, TaskForm

# Create your views here.


@login_required(login_url='/user/login/')
def index(request):
    category_count=Category.objects.count()
    process_count=Process.objects.count()
    activity_count=Activity.objects.count()
    task_count=Task.objects.count()

    context={
        'category_count':category_count,
        'process_count':process_count,
        'activity_count':activity_count,
        'task_count':task_count
    }
    return render(request, 'app/index.html',context)


def category(request):
    if request.method=='POST':
        category_form=CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.instance.user=request.user
            category_form.save()
            messages.add_message(request,messages.INFO,'Kategori eklendi.')
        else:
            messages.add_message(request,messages.INFO,'Kategori eklenirken hata oluştu.')
        return redirect('category')
    
    category_form=CategoryForm()
    categories = Category.objects.order_by('created_date')
    context = {
        'category_form':category_form,
        'categories': categories
    }
    return render(request, 'app/category.html', context)

def category_update(request,category_id):
    category=get_object_or_404(Category,pk=category_id)

    if request.method=='POST':
        category_form=CategoryForm(request.POST,instance=category)
        if category_form.is_valid():
            category_form.instance.user=request.user
            category_form.save()
            messages.add_message(request,messages.INFO,'Kategori güncellendi.')
        else:
            messages.add_message(request,messages.INFO,'Kategori güncellenirken bir hata oluştu.')
        return redirect('category_update',category.id)

    category_form=CategoryForm(instance=category)
    context={
        'category_form':category_form,
        'category':category
    }
    return render(request,'app/category_update.html',context)

def category_delete(request,category_id):
    category=get_object_or_404(Category,pk=category_id)

    if request.method=='POST':
        category.delete()
        messages.add_message(request,messages.INFO, category.name + ' silindi.')
        return redirect('category')
    
    context={
        'category':category
    }
    return render(request,'app/category_delete.html',context)

def category_detail(request,category_id):
    category=get_object_or_404(Category,pk=category_id)
    context={
        'category':category
    }
    return render(request,'app/category_detail.html',context)


def process(request):
    if request.method=='POST':
        process_form=ProcessForm(request.POST)
        if process_form.is_valid():
            process_form.instance.user=request.user
            process_form.save()
            messages.add_message(request,messages.INFO,'İş akışı eklendi.')
        else:
            messages.add_message(request,messages.INFO,'İş akışı eklenirken hata oluştu.')
        return redirect('process')

    process_form=ProcessForm()
    processes = Process.objects.order_by('created_date')
    context = {
        'process_form':process_form,
        'processes': processes
    }
    return render(request, 'app/process.html', context)

def process_update(request,process_id):
    process=get_object_or_404(Process,pk=process_id)

    if request.method=='POST':
        process_form=ProcessForm(request.POST,instance=process)
        if process_form.is_valid():
            process_form.instance.user=request.user
            process_form.save()
            messages.add_message(request,messages.INFO,'İş akışı güncellendi.')
        else:
            messages.add_message(request,messages.INFO,'İş akışı güncellenirken hata oluştu.')
        return redirect('process_update',process_id)
    
    process_form=ProcessForm(instance=process)
    context={
        'process_form':process_form,
        'process':process
    }
    return render(request,'app/process_update.html',context)

def process_delete(request,process_id):
    process=get_object_or_404(Process,pk=process_id)

    if request.method=='POST':
        process.delete()
        messages.add_message(request,messages.INFO, process.name + ' silindi.')
        return redirect('process')
    
    context={
        'process':process
    }
    return render(request,'app/process_delete.html',context)

def activity(request):
    if request.method=='POST':
        activity_form=ActivityForm(request.POST)
        if activity_form.is_valid():
            activity_form.instance.user=request.user
            activity_form.save()
            messages.add_message(request,messages.INFO,'Aktivite eklendi.')
        else:
            messages.add_message(request,messages.INFO,'Aktivite eklenirken hata oluştu.')
        return redirect('activity')
    activity_form=ActivityForm()
    activities = Activity.objects.order_by('created_date')
    context = {
        'activity_form':activity_form,
        'activities': activities
    }
    return render(request, 'app/activity.html', context)

def activity_update(request,activity_id):
    activity=get_object_or_404(Activity,pk=activity_id)

    if request.method=='POST':
        activity_form=ActivityForm(request.POST,instance=activity)
        if activity_form.is_valid():
            activity_form.instance.user=request.user
            activity_form.save()
            messages.add_message(request,messages.INFO,'Aktivite güncellendi.')
        else:
            messages.add_message(request,messages.INFO,'Aktivite güncellenirken hata oluştu.')
        return redirect('activity_update',activity_id)
    
    activity_form=ActivityForm(instance=activity)
    context={
        'activity_form':activity_form,
        'activity':activity
    }
    return render(request,'app/activity_update.html',context)

def activity_delete(request,activity_id):
    activity=get_object_or_404(Activity,pk=activity_id)

    if request.method=='POST':
        activity.delete()
        messages.add_message(request,messages.INFO, activity.name + ' silindi.')
        return redirect('activity')
    
    context={
        'activity':activity
    }
    return render(request,'app/activity_delete.html',context)

def task(request):
    if request.method=='POST':
        task_form=TaskForm(request.POST)
        if task_form.is_valid():
            task_form.instance.user=request.user
            task_form.save()
            messages.add_message(request,messages.INFO,'Görev eklendi.')
        else:
            messages.add_message(request,messages.INFO,'Görev eklenirken hata oluştu.')
        return redirect('task')
    
    task_form=TaskForm()
    tasks = Task.objects.order_by('created_date')
    context = {
        'task_form':task_form,
        'tasks': tasks
    }
    return render(request, 'app/task.html', context)

def task_update(request,task_id):
    task=get_object_or_404(Task,pk=task_id)

    if request.method=='POST':
        task_form=TaskForm(request.POST,instance=task)
        if task_form.is_valid():
            task_form.instance.user=request.user
            task_form.save()
            messages.add_message(request,messages.INFO,'Görev güncellendi.')
        else:
            messages.add_message(request,messages.INFO,'Görev güncellenirken hata oluştu.')
        return redirect('task_update',task_id)
    
    task_form=TaskForm(instance=task)
    context={
        'task_form':task_form,
        'task':task
    }
    return render(request,'app/task_update.html',context)

def task_delete(request,task_id):
    task=get_object_or_404(Task,pk=task_id)

    if request.method=='POST':
        task.delete()
        messages.add_message(request,messages.INFO, task.name + ' silindi.')
        return redirect('task')
    
    context={
        'task':task
    }
    return render(request,'app/task_delete.html',context)