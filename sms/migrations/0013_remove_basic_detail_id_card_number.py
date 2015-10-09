# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0012_basic_detail_id_card_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basic_detail',
            name='id_card_number',
        ),
    ]
