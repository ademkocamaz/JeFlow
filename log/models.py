from django.db import models
import logging
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.

LOG_LEVELS = (
    (logging.NOTSET, _('NotSet')),
    (logging.INFO, _('Info')),
    (logging.WARNING, _('Warning')),
    (logging.DEBUG, _('Debug')),
    (logging.ERROR, _('Error')),
    (logging.FATAL, _('Fatal')),
)

class Log(models.Model):
    logger_name = models.CharField(max_length=100,verbose_name='Loglayıcı Adı')
    level = models.PositiveSmallIntegerField(choices=LOG_LEVELS, default=logging.ERROR, db_index=True,verbose_name='Seviye')
    msg = models.TextField(verbose_name='Mesaj')
    trace = models.TextField(blank=True, null=True,verbose_name='Yığın')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Kullanıcı', blank=True, null=True)

    def __str__(self):
        return self.msg

    class Meta:
        ordering = ('-create_datetime',)
        verbose_name = 'Log'
        verbose_name_plural ='Loglar'

