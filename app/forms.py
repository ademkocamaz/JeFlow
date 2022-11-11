from dataclasses import fields
from django import forms
from .models import Activity, Category,Process,Task, State

# Create your forms here.

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=('name','description')

class ProcessForm(forms.ModelForm):
    class Meta:
        model=Process
        fields=('category','name','description','state')

class ActivityForm(forms.ModelForm):
    class Meta:
        model=Activity
        fields=('process','name','description','observation')

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=('process','name','description','assigned_user','state')

class StateForm(forms.ModelForm):
    class Meta:
        model=State
        fields=('name', 'description')