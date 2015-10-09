# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0013_remove_basic_detail_id_card_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_detail',
            name='id_card_number',
            field=models.CharField(default=b'', unique=True, max_length=50),
        ),
    ]
