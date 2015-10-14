# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0025_basic_detail_middle_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basic_detail',
            name='id_card_number',
        ),
    ]
