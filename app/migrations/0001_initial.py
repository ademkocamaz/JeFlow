# Generated by Django 4.1.2 on 2022-11-01 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='İş Akış Adı')),
                ('description', models.TextField(verbose_name='İş Akış Açıklaması')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
            ],
            options={
                'verbose_name': 'İş Akış Tanımı',
                'verbose_name_plural': 'İş Akış Tanımları',
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='İş Adı')),
                ('description', models.TextField(verbose_name='İş Açıklama')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='İş Akış Tanımı')),
            ],
            options={
                'verbose_name': 'İş Akışı',
                'verbose_name_plural': 'İş Akışları',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Görev Adı')),
                ('description', models.TextField(verbose_name='Görev Açıklaması')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Tamamlandı Mı?')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.process', verbose_name='İş Adı')),
            ],
            options={
                'verbose_name': 'Görev',
                'verbose_name_plural': 'Görevler',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Aktivite Adı')),
                ('description', models.TextField(verbose_name='Aktivite Açıklaması')),
                ('observation', models.TextField(verbose_name='Gözlem')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.process', verbose_name='İş Adı')),
            ],
            options={
                'verbose_name': 'Aktive',
                'verbose_name_plural': 'Aktiviteler',
            },
        ),
    ]
