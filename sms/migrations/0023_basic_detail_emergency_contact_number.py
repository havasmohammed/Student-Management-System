# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0022_auto_20151013_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_detail',
            name='emergency_contact_number',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
