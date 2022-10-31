from django.contrib import admin
from .models import Process, ProcessDetail, Activity

# Register your models here.


class ProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date')
    list_display_links = ('id', 'name')
    list_filter = ('created_date',)
    # list_editable = ('name',)
    search_fields = ('name', 'description')
    list_per_page = 20


class ProcessDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'process', 'created_date')
    list_display_links = ('id', 'name')
    list_filter = ('created_date',)
    search_fields = ('name', 'description')
    list_per_page = 20


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'process_detail', 'created_date')
    list_display_links = ('id', 'name')
    list_filter = ('created_date',)
    search_fields = ('name', 'description')
    list_per_page = 20


admin.site.register(Process, ProcessAdmin)
admin.site.register(ProcessDetail, ProcessDetailAdmin)
admin.site.register(Activity,ActivityAdmin)