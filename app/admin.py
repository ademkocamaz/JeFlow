from django.contrib import admin
from .models import Category, Process, Activity, Task, State

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date', 'user')
    list_display_links = ('id', 'name')
    list_filter = ('created_date',)
    # list_editable = ('user',)
    search_fields = ('name', 'description')
    # list_per_page = 20


class ProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'state', 'created_date', 'user')
    list_display_links = ('id', 'name')
    list_filter = ('created_date',)
    search_fields = ('name', 'description')
    list_editable = ('state',)
    # list_per_page = 20


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'process', 'created_date', 'user')
    list_display_links = ('id', 'name')
    list_filter = ('created_date',)
    search_fields = ('name', 'description','observation')
    # list_editable = ('user',)
    # list_per_page = 20

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'process', 'created_date','state', 'user')
    list_display_links = ('id', 'name')
    list_filter = ('created_date',)
    list_editable = ('state',)
    search_fields = ('name', 'description')
    # list_per_page = 20

class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','color')
    list_display_links = ('id','name')
    list_editable = ('color',)
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Process, ProcessAdmin)
admin.site.register(Activity,ActivityAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(State,StateAdmin)