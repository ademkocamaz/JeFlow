from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('category/',views.category,name='category'),
    path('category/<int:category_id>', views.category_detail, name='category_detail'),
    path('process/',views.process,name='process'),
    path('process/<int:process_id>', views.process_detail, name='process_detail'),
    path('activity/',views.activity,name='activity'),
    path('activity/<int:activity_id>', views.activity_detail, name='activity_detail'),
    path('task/',views.task,name='task'),
    path('task/<int:task_id>', views.task_detail, name='task_detail'),
]