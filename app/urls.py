from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    
    path('category/', views.category, name='category'),
    path('category/<int:category_id>', views.category_detail, name='category_detail'),
    path('category/<int:category_id>/delete', views.category_delete, name='category_delete'),

    path('process/', views.process, name='process'),
    path('process/<int:process_id>', views.process_detail, name='process_detail'),
    path('process/<int:process_id>/delete', views.process_delete, name='process_delete'),
    
    path('activity/', views.activity, name='activity'),
    path('activity/<int:activity_id>', views.activity_detail, name='activity_detail'),
    path('activity/<int:activity_id>/delete', views.activity_delete, name='activity_delete'),
    
    path('task/', views.task, name='task'),
    path('task/<int:task_id>', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/delete', views.task_delete, name='task_delete'),
]