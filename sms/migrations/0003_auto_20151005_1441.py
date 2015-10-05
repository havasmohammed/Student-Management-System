# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20151005_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_detail',
            name='father_name',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='basic_detail',
            name='mothername',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
