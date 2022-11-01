# Generated by Django 4.1.2 on 2022-11-01 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Durumu'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Aktivite Açıklaması'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='observation',
            field=models.TextField(blank=True, null=True, verbose_name='Gözlem'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='İş Akış Açıklaması'),
        ),
        migrations.AlterField(
            model_name='process',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='İş Açıklama'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Görev Açıklaması'),
        ),
    ]