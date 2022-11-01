from dataclasses import fields
from django import forms
from .models import Category,Process

# Create your forms here.

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=('name','description')

class ProcessForm(forms.ModelForm):
    class Meta:
        model=Process
        fields=('category','name','description','state')