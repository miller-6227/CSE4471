# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20160415_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='file_directory',
            field=models.CharField(default='/Users/Desktop', max_length=1000),
        ),
        migrations.AddField(
            model_name='user',
            name='ip_address',
            field=models.CharField(default='11', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='port_number',
            field=models.CharField(default='6000', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, default=None, related_name='_user_friends_+', to='login.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
