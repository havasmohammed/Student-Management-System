# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0006_basic_detail_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login_page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sid', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
