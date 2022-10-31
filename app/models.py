from django.db import models

# Create your models here.

class Process(models.Model):
    name=models.CharField(max_length=500,verbose_name='İş Akış Adı')
    description=models.TextField(verbose_name='İş Akış Açıklaması')
    created_date=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')

    def __str__(self):
        return self.name # + ' - ' + self.created_date.strftime("%d.%m.%Y, %H:%M:%S")
    
    class Meta:
        verbose_name='İş Akış Tanımı'
        verbose_name_plural="İş Akış Tanımları"

class ProcessDetail(models.Model):
    process=models.ForeignKey(Process,on_delete=models.CASCADE,verbose_name='İş Akış Tanımı')
    name=models.CharField(max_length=500,verbose_name='İş Adı')
    description=models.TextField(verbose_name='İş Açıklama')
    created_date=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')

    def __str__(self):
        return self.name # + ' - ' + self.created_date.strftime("%d.%m.%Y, %H:%M:%S")
    
    class Meta:
        verbose_name="İş Akışı"
        verbose_name_plural='İş Akışları'

class Activity(models.Model):
    process_detail=models.ForeignKey(ProcessDetail,on_delete=models.CASCADE,verbose_name='İş Adı')
    name=models.CharField(max_length=500,verbose_name='Aktivite Adı')
    description=models.TextField(verbose_name='Aktivite Açıklaması')
    observation=models.TextField(verbose_name='Gözlem')
    created_date=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')

    def __str__(self):
        return self.name # + ' - ' + self.created_date.strftime("%d.%m.%Y, %H:%M:%S")
        
    class Meta:
        verbose_name="Aktive"
        verbose_name_plural='Aktiviteler'