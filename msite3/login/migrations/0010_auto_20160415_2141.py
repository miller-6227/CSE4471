# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20160415_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='friends',
        ),
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='_user_friends_+', to='login.User'),
        ),
    ]
