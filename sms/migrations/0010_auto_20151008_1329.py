# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0009_auto_20151008_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_detail',
            name='id_card_number',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
