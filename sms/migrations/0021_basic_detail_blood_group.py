# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0020_auto_20151013_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_detail',
            name='blood_group',
            field=models.CharField(blank=True, max_length=4, null=True, choices=[(b'O+', b'O+'), (b'O-', b'O-'), (b'A+', b'A+'), (b'A-', b'A-'), (b'B+', b'B+'), (b'B-', b'B-'), (b'AB+', b'AB+'), (b'AB-', b'AB-')]),
        ),
    ]
