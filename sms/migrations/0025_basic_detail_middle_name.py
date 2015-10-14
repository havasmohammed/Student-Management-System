# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0024_miscellaneous_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_detail',
            name='middle_name',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
