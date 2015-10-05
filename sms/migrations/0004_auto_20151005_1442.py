# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_auto_20151005_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basic_detail',
            old_name='mothername',
            new_name='mother_name',
        ),
    ]
