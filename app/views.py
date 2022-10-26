from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/user/login/')
def index(request):    
    return render(request,'app/index.html')