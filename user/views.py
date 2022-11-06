from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
import logging
# Create your views here.
logger=logging.getLogger('db')

def login(request):
    messages.add_message(request,messages.INFO,'demo / demo ile giriş yapabilirsiniz')
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
