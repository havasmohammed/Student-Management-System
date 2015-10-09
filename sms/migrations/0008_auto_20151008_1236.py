# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0007_login_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login_page',
            name='id',
        ),
        migrations.AlterField(
            model_name='login_page',
            name='sid',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
