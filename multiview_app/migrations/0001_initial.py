# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 14:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='pics/none/no-img.jpg', upload_to='pics/')),
                ('name', models.CharField(blank=True, default='No Name', max_length=200)),
                ('ssim', models.CharField(blank=True, max_length=100, null=True)),
                ('mse', models.CharField(blank=True, max_length=100, null=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
