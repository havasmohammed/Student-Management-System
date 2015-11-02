# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0037_auto_20151102_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetail',
            name='semester',
            field=models.CharField(default=b'', max_length=5, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8')]),
        ),
    ]
