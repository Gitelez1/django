# Generated by Django 5.1 on 2024-08-12 14:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='show',
            name='network',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='show',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='show',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
