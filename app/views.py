from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    messages.add_message(request,messages.INFO,'Hoşgeldiniz.')
    return render(request,'app/index.html')