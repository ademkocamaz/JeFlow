from django.contrib import admin
from .models import Category, Process, Activity, Task

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date')
    list_display_links = ('id', 'name')
    list_filter = ('created_date',)
    # list_editable = ('name',)
    search_fields = ('name', 'description')
    # list_per_page = 20


class ProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'state', 'created_date')
    list_display_links = ('id', 'name')
    list_filter = ('created_date',)
    search_fields = ('name', 'description')
    # list_per_page = 20


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'process', 'created_date')
    list_display_links = ('id', 'name')
    list_filter = ('created_date',)
    search_fields = ('name', 'description','observation')
    # list_per_page = 20

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'process', 'created_date','is_completed')
    list_display_links = ('id', 'name')
    list_filter = ('created_date',)
    list_editable = ('is_completed',)
    search_fields = ('name', 'description')
    # list_per_page = 20


admin.site.register(Category, CategoryAdmin)
admin.site.register(Process, ProcessAdmin)
admin.site.register(Activity,ActivityAdmin)
admin.site.register(Task,TaskAdmin)