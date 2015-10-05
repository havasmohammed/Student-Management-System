# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0004_auto_20151005_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnum', models.CharField(max_length=9)),
                ('cname', models.CharField(max_length=50)),
                ('credits', models.IntegerField()),
                ('year_of_registration', models.BigIntegerField()),
            ],
        ),
    ]
