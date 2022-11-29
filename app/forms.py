from django import forms
from .models import Activity, Category,Process,Task, State

# Create your forms here.

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=('name','description')
        # fields = '__all__'

class ProcessForm(forms.ModelForm):
    class Meta:
        model=Process
        fields=('category','name','description','state', 'file')

class ActivityForm(forms.ModelForm):
    class Meta:
        model=Activity
        fields=('process','name','description','observation', 'file')

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=('process','name','description','assigned_user','state', 'file')

class StateForm(forms.ModelForm):
    class Meta:
        model=State
        fields=('name', 'color', 'description')