# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0019_auto_20151013_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_detail',
            name='gender',
            field=models.CharField(default=b'M', max_length=2, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
