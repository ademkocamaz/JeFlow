from django.contrib import admin
from .models import Log
from .config import DJANGO_DB_LOGGER_ADMIN_LIST_PER_PAGE
import logging
from django.utils.html import format_html

# Register your models here.
class LogAdmin(admin.ModelAdmin):
    # list_display=('id','logger_name','level','msg','trace','create_datetime')
    list_display = ('id', 'logger_name', 'level', 'colored_msg', 'traceback', 'create_datetime_format','user')
    #list_display_links = ('id', 'logger_name')
    list_display_links = ('colored_msg', )
    list_filter = ('level','create_datetime','user')
    search_fields = ('logger_name', 'level','msg')
    list_per_page = DJANGO_DB_LOGGER_ADMIN_LIST_PER_PAGE

    def colored_msg(self, instance):
        if instance.level in [logging.NOTSET, logging.INFO]:
            color = 'white'
        elif instance.level in [logging.WARNING, logging.DEBUG]:
            color = 'orange'
        else:
            color = 'red'
        return format_html('<span style="color: {color};">{msg}</span>', color=color, msg=instance.msg)
    colored_msg.short_description = 'Mesaj'

    def traceback(self, instance):
        return format_html('<pre><code>{content}</code></pre>', content=instance.trace if instance.trace else '')

    def create_datetime_format(self, instance):
        return instance.create_datetime.strftime('%Y-%m-%d %X')
    create_datetime_format.short_description = 'Oluşturulma Zamanı'

admin.site.register(Log,LogAdmin)