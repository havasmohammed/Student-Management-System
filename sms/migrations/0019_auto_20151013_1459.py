# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0018_auto_20151013_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_detail',
            name='code',
            field=models.CharField(default=b'', help_text=b'Code of the stream', unique=True, max_length=10),
        ),
    ]
