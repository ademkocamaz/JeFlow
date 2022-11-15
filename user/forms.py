from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields=('username','first_name','last_name','email')

class ResetPasswordForm(SetPasswordForm):
    class Meta:
        model=get_user_model()
        fields=('new_password1','new_password2')

class TestForm(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields=('__all__')