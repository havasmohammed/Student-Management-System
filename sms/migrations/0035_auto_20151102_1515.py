# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0034_auto_20151102_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetail',
            name='branch',
            field=models.CharField(default=b'', max_length=20, choices=[(b'IT', b'IT'), (b'CSE', b'CSE'), (b'ECE', b'ECE'), (b'CE', b'CE'), (b'PE', b'PE'), (b'ME', b'ME'), (b'EE', b'EE'), (b'BT', b'BT')]),
        ),
    ]
