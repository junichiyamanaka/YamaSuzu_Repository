# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-02 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horse', models.CharField(max_length=100)),
                ('f_horse', models.CharField(max_length=100)),
                ('m_horse', models.CharField(max_length=100)),
                ('ff_horse', models.CharField(max_length=100)),
                ('fm_horse', models.CharField(max_length=100)),
                ('mf_horse', models.CharField(max_length=100)),
                ('mm_horse', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
