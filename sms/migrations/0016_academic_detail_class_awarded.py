# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0015_academic_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='academic_detail',
            name='Class_awarded',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
