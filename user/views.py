from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from .forms import ProfileForm, ResetPasswordForm
import logging
# Create your views here.
logger=logging.getLogger('db')

def login(request):
    messages.add_message(request,messages.INFO,'Kullanıcı Adı: demo Şifre: demo ile giriş yapabilirsiniz')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.add_message(request,messages.SUCCESS, 'Oturum açıldı.')
            messages.add_message(request,messages.INFO, username + ' Hoşgeldiniz.')
            logger.info(username + ' kullanıcı adı ile oturum açıldı.')
            return redirect('index')
        else:
            messages.add_message(request,messages.ERROR, 'Kullanıcı adı veya Parola yanlış')
            logger.error(username + ' kullanıcı adı ile oturum açılırken hata oluştu.')
    
    return render(request, 'user/login.html')
    
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['repassword']

        if password==repassword:
            if User.objects.filter(username=username).exists():
                messages.add_message(request,messages.WARNING,username+' Kullanıcı adı sistemde kayıtlı.')
                logger.error(username + ' kullanıcı adı ile kayıt olurken hata oluştu. Sistemde kayıtlı.')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request,messages.WARNING,email+' E-mail adresi sistemde kayıtlı.')
                    logger.error(email + ' email adresi ile kayıt olurken hata oluştu. Sistemde kayıtlı.')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    messages.add_message(request,messages.SUCCESS,username+' Hesabınız başarıyla oluşturuldu')
                    logger.info(username + ' kullanıcı adı ile kayıt başarı ile oluşturuldu.')
                    return redirect('login')
        else:
            messages.add_message(request,messages.ERROR,'Parolalar eşleşmiyor')
            return redirect('register')

    return render(request,'user/register.html')

def logout(request):
    if request.method=='POST':
        username=request.user.username
        auth.logout(request)
        messages.add_message(request,messages.SUCCESS,'Oturumunuz kapatıldı.')
        logger.info(username + ' oturumu kapatıldı.')
    return redirect('index')

@login_required(login_url='/user/login/')
def profile(request):
    if request.method=='POST':
        profile_form=ProfileForm(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.add_message(request,messages.INFO,'Kullanıcı bilgileri güncellendi.')
            logger.info(request.user.username+' adında kullanıcı bilgileri güncellendi.',extra={'user':request.user})
        else:
            messages.add_message(request,messages.INFO,'Kullanıcı bilgileri güncellenirken bir hata oluştu.')
            logger.error(request.user.username+' adında kullanıcı bilgileri güncellenirken bir hata oluştu.',extra={'user':request.user})

    profile_form=ProfileForm(instance=request.user)
    context={
        'profile_form':profile_form,
    }
    return render(request,'user/profile.html',context)

@login_required(login_url='/user/login/')
def reset_password(request):
    if request.method=='POST':
        reset_password_form=ResetPasswordForm(request.user,request.POST)
        if reset_password_form.is_valid():
            reset_password_form.save()
            messages.add_message(request,messages.INFO,'Şifreniz başarıyla değiştirildi.')
            logger.info(request.user.username+' şifre değiştirildi',extra={'user':request.user})
        else:
            messages.add_message(request,messages.ERROR,'Şifreniz değiştirilirken hata oluştu.')
            logger.error(request.user.username+' şifre değiştirilirken hata oluştu.',extra={'user':request.user})
            for error in list(reset_password_form.errors.values()):
                messages.add_message(request,messages.ERROR,error)
    reset_password_form=ResetPasswordForm(request.user)
    context={
        'reset_password_form':reset_password_form
    }
    return render(request,'user/reset_password.html',context)
