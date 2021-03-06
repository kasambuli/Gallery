# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-04 08:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image_name']},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={},
        ),
        migrations.AlterField(
            model_name='image',
            name='image_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygallery.Category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygallery.Location'),
        ),
    ]
