# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-07 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resanal', '0009_auto_20181003_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.IntegerField()),
                ('sem', models.IntegerField()),
                ('sec', models.CharField(max_length=1)),
                ('passCount', models.FloatField()),
                ('failCount', models.FloatField()),
                ('totalCount', models.FloatField()),
                ('average', models.FloatField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='analysis',
            unique_together=set([('batch', 'sem', 'sec')]),
        ),
    ]