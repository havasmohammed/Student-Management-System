# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0008_auto_20151008_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basic_detail',
            name='id',
        ),
        migrations.AddField(
            model_name='basic_detail',
            name='id_card_number',
            field=models.CharField(default=b'', unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='basic_detail',
            name='sid',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
