# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-07 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0157_set_new_contributors_welcome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalapplication',
            name='community_specific_questions',
            field=models.TextField(blank=True, help_text='Some communities or projects may want you to answer additional questions. Please check with your mentor and community coordinator to see if you need to provide any additional information after you save your final application.', max_length=8000, verbose_name='(Optional) Community-specific Questions'),
        ),
    ]