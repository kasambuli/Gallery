# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-06 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery', '0002_auto_20180504_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_url',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='gallery/'),
        ),
    ]
