from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('category/',views.category,name='category'),
    path('process/',views.process,name='process'),
    path('activity/',views.activity,name='activity'),
    path('task/',views.task,name='task'),
]