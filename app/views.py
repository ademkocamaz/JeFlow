from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Category, Process, Activity, Task, State
from log.models import Log
from .forms import CategoryForm, ProcessForm, ActivityForm, TaskForm, StateForm
import logging
# Create your views here.

logger=logging.getLogger('db')

@login_required(login_url='/user/login/')
def index(request):
    category_count=Category.objects.count()
    process_count=Process.objects.count()
    activity_count=Activity.objects.count()
    task_count=Task.objects.count()
    user_activities=Log.objects.all().filter(user=request.user)[:10]

    context={
        'category_count':category_count,
        'process_count':process_count,
        'activity_count':activity_count,
        'task_count':task_count,
        'user_activities':user_activities
    }
    return render(request, 'app/index.html', context)

@login_required(login_url='/user/login/')
def settings(request):
    state_form=StateForm()
    states=State.objects.order_by('created_date')
    context={
        'state_form':state_form,
        'states':states,
    }
    return render(request,'app/settings.html',context)

@login_required(login_url='/user/login/')
def category(request):
    if request.method=='POST':
        category_form=CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.instance.user=request.user
            category_form.save()
            messages.add_message(request,messages.INFO,'Kategori eklendi.')
            logger.info(category_form.instance.name+' adında Kategori eklendi.', extra={'user':request.user})
        else:
            messages.add_message(request,messages.ERROR,'Kategori eklenirken hata oluştu.')
            logger.error(category_form.instance.name+' adında Kategori eklenirken hata oluştu.', extra={'user':request.user})
            for error in list(category_form.errors.values()):
                messages.add_message(request,messages.ERROR,error)
        return redirect('category')
    
    category_form=CategoryForm()
    categories = Category.objects.order_by('-created_date')
    
    context = {
        'category_form':category_form,
        'categories': categories,
    }
    return render(request, 'app/category.html', context)

@login_required(login_url='/user/login/')
def category_update(request,category_id):
    category=get_object_or_404(Category,pk=category_id)

    if request.method=='POST':
        category_form=CategoryForm(request.POST,instance=category)
        if category_form.is_valid():
            category_form.instance.user=request.user
            category_form.save()
            messages.add_message(request,messages.INFO,'Kategori güncellendi.')
            logger.info(category.name+' adında kategori güncellendi.',extra={'user':request.user})
        else:
            messages.add_message(request,messages.INFO,'Kategori güncellenirken bir hata oluştu.')
            logger.error(category.name+' adında kategori güncellenirken bir hata oluştu.',extra={'user':request.user})
            for error in list(category_form.errors.values()):
                messages.add_message(request,messages.ERROR,error)
        # return redirect('category_update',category.id)
        return redirect('category')

    category_form=CategoryForm(instance=category)
    context={
        'category_form':category_form,
        'category':category
    }
    return render(request,'app/category_update.html',context)

@login_required(login_url='/user/login/')
def category_delete(request,category_id):
    category=get_object_or_404(Category,pk=category_id)

    if request.method=='POST':
        category.delete()
        messages.add_message(request,messages.INFO, category.name + ' silindi.')
        logger.info(category.name+' adında kategori silindi.',extra={'user':request.user})
        return redirect('category')
    
    context={
        'category':category
    }
    return render(request,'app/category_delete.html',context)

@login_required(login_url='/user/login/')
def category_detail(request,category_id):
    category=get_object_or_404(Category,pk=category_id)
    processes=Process.objects.all().filter(category=category)

    if request.method=='POST':
        process_form=ProcessForm(request.POST, request.FILES)
        if process_form.is_valid():
            process_form.instance.user=request.user
            process_form.save()
            messages.add_message(request,messages.INFO,'İş akışı eklendi.')
            logger.info(process_form.instance.name+' adında İş Akışı eklendi.',extra={'user':request.user})
        else:
            messages.add_message(request,messages.INFO,'İş akışı eklenirken hata oluştu.')
            logger.error(process_form.instance.name+' adında İş Akışı eklenirken hata oluştu.',extra={'user':request.user})
            for error in list(process_form.errors.values()):
                messages.add_message(request,messages.ERROR,error)
        return redirect('category_detail',category.id)
    state=get_object_or_404(State,name='Yeni')
    process_form=ProcessForm(initial={'category':category,'state':state})
    context={
        'category':category,
        'processes':processes,
        'process_form':process_form,
    }
    return render(request,'app/category_detail.html',context)

@login_required(login_url='/user/login/')
def process(request):
    if request.method=='POST':
        process_form=ProcessForm(request.POST, request.FILES)
        if process_form.is_valid():
            process_form.instance.user=request.user
            process_form.save()
            messages.add_message(request,messages.INFO,'İş akışı eklendi.')
            logger.info(process_form.instance.name+' adında İş Akışı eklendi.',extra={'user':request.user})
        else:
            messages.add_message(request,messages.INFO,'İş akışı eklenirken hata oluştu.')
            logger.error(process_form.instance.name+' adında İş Akışı eklenirken hata oluştu.',extra={'user':request.user})
            for error in list(process_form.errors.values()):
                messages.add_message(request,messages.ERROR,error)
        return redirect('process')

    state=get_object_or_404(State,name='Yeni')
    process_form=ProcessForm(initial={'state':state})
    processes = Process.objects.order_by('-created_date')
    context = {
        'process_form':process_form,
        'processes': processes
    }
    return render(request, 'app/process.html', context)

@login_required(login_url='/user/login/')
def process_update(request,process_id):
    process=get_object_or_404(Process,pk=process_id)

    if request.method=='POST':
        process_form=ProcessForm(request.POST, request.FILES, instance=process)
        if process_form.is_valid():
            process_form.instance.user=request.user
            process_form.save()
            messages.add_message(request,messages.INFO,'İş akışı güncellendi.')
            logger.info(process.name+' adında İş Akışı güncellendi',extra={'user':request.user})
        else:
            messages.add_message(request,messages.INFO,'İş akışı güncellenirken hata oluştu.')
            logger.error(process.name+' adında İş Akışı güncellenirken hata oluştu.',extra={'user':request.user})
            for error in list(process_form.errors.values()):
                messages.add_message(request,messages.ERROR,error)
        # return redirect('process_update',process_id)
        return redirect('process')
    
    process_form=ProcessForm(instance=process)
    context={
        'process_form':process_form,
        'process':process
    }
    return render(request,'app/process_update.html',context)

@login_required(login_url='/user/login/')
def process_delete(request,process_id):
    process=get_object_or_404(Process,pk=process_id)

    if request.method=='POST':
        process.delete()
        messages.add_message(request,messages.INFO, process.name + ' silindi.')
        logger.info(process.name+' adında İş Akışı silindi',extra={'user':request.user})
        return redirect('process')
    
    context={
        'process':process
    }
    return render(request,'app/process_delete.html',context)

@login_required(login_url='/user/login/')
def process_detail(request,process_id):
    process=get_object_or_404(Process,pk=process_id)
    activities=Activity.objects.all().filter(process=process)
    tasks=Task.objects.all().filter(process=process)

    context={
        'process':process,
        'activities':activities,
        'tasks':tasks,
    }
    return render(request,'app/process_detail.html',context)

@login_required(login_url='/user/login/')
def activity(request):
    if request.method=='POST':
        activity_form=ActivityForm(request.POST, request.FILES)
        if activity_form.is_valid():
            activity_form.instance.user=request.user
            activity_form.save()
            messages.add_message(request,messages.INFO,'Aktivite eklendi.')
            logger.info(activity_form.instance.name+' adında Aktivite eklendi.',extra={'user':request.user})
        else:
            messages.add_message(request,messages.INFO,'Aktivite eklenirken hata oluştu.')
            logger.error(activity_form.instance.name+' adında Aktivite eklenirken hata oluştu.',extra={'user':request.user})
            for error in list(activity_form.errors.values()):
                messages.add_message(request,messages.ERROR,error)
        return redirect('activity')
    activity_form=ActivityForm()
    activities = Activity.objects.order_by('-created_date')
    context = {
        'activity_form':activity_form,
        'activities': activities
    }
    return render(request, 'app/activity.html', context)

@login_required(login_url='/user/login/')
def activity_update(request,activity_id):
    activity=get_object_or_404(Activity,pk=activity_id)

    if request.method=='POST':
        activity_form=ActivityForm(request.POST, request.FILES, instance=activity)
        if activity_form.is_valid():
            activity_form.instance.user=request.user
            activity_form.save()
            messages.add_message(request,messages.INFO,'Aktivite güncellendi.')
            logger.info(activity.name+' adında Aktivite güncellendi.',extra={'user':request.user})
        else:
            messages.add_message(request,messages.INFO,'Aktivite güncellenirken hata oluştu.')
            logger.error(activity.name+' adında Aktivite güncellenirken hata oluştu.', extra={'user':request.user})
            for error in list(activity_form.errors.values()):
                messages.add_message(request,messages.ERROR,error)
        # return redirect('activity_update',activity_id)
        return redirect('activity')
    
    activity_form=ActivityForm(instance=activity)
    context={
        'activity_form':activity_form,
        'activity':activity
    }
    return render(request,'app/activity_update.html',context)

@login_required(login_url='/user/login/')
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

@login_required(login_url='/user/login/')
def activity_detail(request,activity_id):
    activity=get_object_or_404(Activity,pk=activity_id)

    context={
        'activity':activity,
    }
    return render(request,'app/activity_detail.html',context)

@login_required(login_url='/user/login/')
def task(request):
    if request.method=='POST':
        task_form=TaskForm(request.POST, request.FILES)
        if task_form.is_valid():
            task_form.instance.user=request.user
            task_form.save()
            messages.add_message(request,messages.INFO,'Görev eklendi.')
            logger.info(task_form.instance.name+' adında Görev eklendi.',extra={'user':request.user})
        else:
            messages.add_message(request,messages.INFO,'Görev eklenirken hata oluştu.')
            logger.error(task_form.instance.name+' adında Görev eklenirken hata oluştu.',extra={'user':request.user})
            for error in list(task_form.errors.values()):
                messages.add_message(request,messages.ERROR,error)
        return redirect('task')
    state=get_object_or_404(State,name='Yeni')
    task_form=TaskForm(initial={'state':state})
    tasks = Task.objects.order_by('-created_date')
    context = {
        'task_form':task_form,
        'tasks': tasks
    }
    return render(request, 'app/task.html', context)

@login_required(login_url='/user/login/')
def task_update(request,task_id):
    task=get_object_or_404(Task,pk=task_id)

    if request.method=='POST':
        task_form=TaskForm(request.POST, request.FILES, instance=task)
        if task_form.is_valid():
            task_form.instance.user=request.user
            task_form.save()
            messages.add_message(request,messages.INFO,'Görev güncellendi.')
            logger.info(task.name+' adında Görev güncellendi.',extra={'user':request.user})
        else:
            messages.add_message(request,messages.INFO,'Görev güncellenirken hata oluştu.')
            logger.error(task.name+' adında Görev güncellenirken hata oluştu.',extra={'user':request.user})
            for error in list(task_form.errors.values()):
                messages.add_message(request,messages.ERROR,error)
        # return redirect('task_update',task_id)
        return redirect('task')
    
    task_form=TaskForm(instance=task)
    context={
        'task_form':task_form,
        'task':task
    }
    return render(request,'app/task_update.html',context)

@login_required(login_url='/user/login/')
def task_delete(request,task_id):
    task=get_object_or_404(Task,pk=task_id)

    if request.method=='POST':
        task.delete()
        messages.add_message(request,messages.INFO, task.name + ' silindi.')
        logger.info(task.name+' adında Görev silindi.',extra={'user':request.user})
        return redirect('task')
    
    context={
        'task':task
    }
    return render(request,'app/task_delete.html',context)

@login_required(login_url='/user/login/')
def task_detail(request,task_id):
    task=get_object_or_404(Task,pk=task_id)

    context={
        'task':task,
    }
    return render(request,'app/task_detail.html',context)

@login_required(login_url='/user/login/')
def state(request):
    if request.method=='POST':
        state_form=StateForm(request.POST)
        if state_form.is_valid():
            state_form.instance.user=request.user
            state_form.save()
            messages.add_message(request,messages.INFO,'Durum eklendi.')
            logger.info(state_form.instance.name+' adında Durum eklendi.',extra={'user':request.user})
        else:
            messages.add_message(request,messages.INFO,'Durum eklenirken hata oluştu.')
            logger.error(state_form.instance.name+' adında Durum eklenirken hata oluştu.',extra={'user':request.user})
            for error in list(state_form.errors.values()):
                messages.add_message(request,messages.ERROR,error)
        return redirect('state')
    state_form=StateForm()
    states = State.objects.order_by('-created_date')
    context = {
        'state_form':state_form,
        'states': states
    }
    return render(request, 'app/state.html', context)

@login_required(login_url='/user/login/')
def state_update(request,state_id):
    state=get_object_or_404(State,pk=state_id)

    if request.method=='POST':
        state_form=StateForm(request.POST,instance=state)
        if state_form.is_valid():
            state_form.instance.user=request.user
            state_form.save()
            messages.add_message(request,messages.INFO,'Durum güncellendi.')
            logger.info(state.name+' adında Durum güncellendi.',extra={'user':request.user})
        else:
            messages.add_message(request,messages.INFO,'Durum güncellenirken hata oluştu.')
            logger.error(state.name+' adında Durum güncellenirken hata oluştu.',extra={'user':request.user})
            for error in list(state_form.errors.values()):
                messages.add_message(request,messages.ERROR,error)
        # return redirect('state_update',state_id)
        return redirect('state')
    
    state_form=StateForm(instance=state)
    context={
        'state_form':state_form,
        'state':state
    }
    return render(request,'app/state_update.html',context)

@login_required(login_url='/user/login/')
def state_delete(request,state_id):
    state=get_object_or_404(State,pk=state_id)

    if request.method=='POST':
        state.delete()
        messages.add_message(request,messages.INFO, state.name + ' silindi.')
        logger.info(state.name+' adında Durum silindi.',extra={'user':request.user})
        return redirect('state')
    
    context={
        'state':state
    }
    return render(request,'app/state_delete.html',context)

def my_tasks(request):
    state=get_object_or_404(State,name='Yeni')
    task_form=TaskForm(initial={'state':state, 'assigned_user':request.user})
    tasks = Task.objects.all().filter(assigned_user=request.user).order_by('-created_date')
    context = {
        'task_form':task_form,
        'tasks': tasks
    }
    return render(request, 'app/task.html', context)