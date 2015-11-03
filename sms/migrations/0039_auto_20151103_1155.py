# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0038_coursedetail_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetail',
            name='amount_paid',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='coursedetail',
            name='session_fee',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
