from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Category, Process, Activity, Task
from .forms import CategoryForm, ProcessForm

# Create your views here.


@login_required(login_url='/user/login/')
def index(request):
    return render(request, 'app/index.html')


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

def category_detail(request,category_id):
    category=get_object_or_404(Category,pk=category_id)

    if request.method=='POST':
        category_form=CategoryForm(request.POST,instance=category)
        if category_form.is_valid():
            category_form.instance.user=request.user
            category_form.save()
            messages.add_message(request,messages.INFO,'Kategori güncellendi.')
        else:
            messages.add_message(request,messages.INFO,'Kategori güncellenirken bir hata oluştu.')
        return redirect('category_detail',category.id)

    category_form=CategoryForm(instance=category)
    context={
        'category_form':category_form,
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

def process_detail(request,process_id):
    process=get_object_or_404(Process,pk=process_id)

    if request.method=='POST':
        process_form=ProcessForm(request.POST,instance=process)
        if process_form.is_valid():
            process_form.instance.user=request.user
            process_form.save()
            messages.add_message(request,messages.INFO,'İş akışı güncellendi.')
        else:
            messages.add_message(request,messages.INFO,'İş akışı güncellenirken hata oluştu.')
        return redirect('process_detail',process_id)
    
    process_form=ProcessForm(instance=process)
    context={
        'process_form':process_form,
        'process':process
    }
    return render(request,'app/process_detail.html',context)

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
