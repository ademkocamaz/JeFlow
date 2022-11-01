from dataclasses import fields
from django import forms
from .models import Category

# Create your forms here.

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=('name','description')