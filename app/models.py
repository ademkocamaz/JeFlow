from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class State(models.Model):
    name=models.CharField(max_length=100,verbose_name='Durum')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Durum'
        verbose_name_plural='Durumlar'
        
class Category(models.Model):
    name=models.CharField(max_length=500,verbose_name='Kategori Adı')
    description=models.TextField(verbose_name='Kategori Açıklaması', blank=True, null=True)
    created_date=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Kullanıcı', blank=True, null=True)

    def __str__(self):
        return self.name # + ' - ' + self.created_date.strftime("%d.%m.%Y, %H:%M:%S")
    
    class Meta:
        verbose_name='Kategori'
        verbose_name_plural="Kategoriler"

class Process(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Kategori')
    name=models.CharField(max_length=500,verbose_name='İş Akış Adı')
    description=models.TextField(verbose_name='İş Akış Açıklaması', blank=True, null=True)
    state=models.OneToOneField(State, on_delete=models.SET_NULL,verbose_name='Durum', blank=True, null=True)
    created_date=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Kullanıcı', blank=True, null=True)

    def __str__(self):
        return self.name # + ' - ' + self.created_date.strftime("%d.%m.%Y, %H:%M:%S")
    
    class Meta:
        verbose_name='İş Akışı'
        verbose_name_plural='İş Akışları'

class Activity(models.Model):
    process=models.ForeignKey(Process,on_delete=models.CASCADE,verbose_name='İş Adı')
    name=models.CharField(max_length=500,verbose_name='Aktivite Adı')
    description=models.TextField(verbose_name='Aktivite Açıklaması', blank=True,null=True)
    observation=models.TextField(verbose_name='Gözlem', blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Kullanıcı', blank=True, null=True)

    def __str__(self):
        return self.name # + ' - ' + self.created_date.strftime("%d.%m.%Y, %H:%M:%S")
        
    class Meta:
        verbose_name='Aktive'
        verbose_name_plural='Aktiviteler'

class Task(models.Model):
    process=models.ForeignKey(Process,on_delete=models.CASCADE,verbose_name='İş Adı')
    name=models.CharField(max_length=500,verbose_name='Görev Adı')
    description=models.TextField(verbose_name='Görev Açıklaması', blank=True, null=True)
    state=models.OneToOneField(State, on_delete=models.SET_NULL,verbose_name='Durum', blank=True, null=True)
    assigned_user=models.OneToOneField(User,on_delete=models.SET_NULL,related_name='assigned_user',verbose_name='Atanan Personel', blank=True, null=True)
    created_date=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Kullanıcı', blank=True, null=True)

    def __str__(self):
        return self.name # + ' - ' + self.created_date.strftime("%d.%m.%Y, %H:%M:%S")

    class Meta:
        verbose_name='Görev'
        verbose_name_plural='Görevler'

