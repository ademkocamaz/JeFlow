from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('category/', views.category, name='category'),
    path('category/<int:category_id>/detail',
         views.category_detail, name='category_detail'),
    path('category/<int:category_id>/update',
         views.category_update, name='category_update'),
    path('category/<int:category_id>/delete',
         views.category_delete, name='category_delete'),

    path('process/', views.process, name='process'),
    path('process/<int:process_id>/detail',
         views.process_detail, name='process_detail'),
    path('process/<int:process_id>/update',
         views.process_update, name='process_update'),
    path('process/<int:process_id>/delete',
         views.process_delete, name='process_delete'),

    path('activity/', views.activity, name='activity'),
    path('activity/<int:activity_id>/detail',
         views.activity_detail, name='activity_detail'),
    path('activity/<int:activity_id>/update',
         views.activity_update, name='activity_update'),
    path('activity/<int:activity_id>/delete',
         views.activity_delete, name='activity_delete'),

    path('task/', views.task, name='task'),
    path('task/<int:task_id>/detail', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/update', views.task_update, name='task_update'),
    path('task/<int:task_id>/delete', views.task_delete, name='task_delete'),

    path('state', views.state, name='state'),
    path('state/<int:state_id>/update', views.state_update, name='state_update'),
    path('state/<int:state_id>/delete', views.state_delete, name='state_delete'),

    path('settings/', views.settings, name='settings'),

    path('my-tasks/', views.my_tasks, name='my_tasks')


]
