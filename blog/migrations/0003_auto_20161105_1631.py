# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='docfile',
            field=models.FileField(null=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]
