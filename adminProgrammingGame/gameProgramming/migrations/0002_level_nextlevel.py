# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-28 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameProgramming', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='nextLevel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gameProgramming.Level'),
        ),
    ]