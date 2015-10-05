# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0005_course_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_detail',
            name='email',
            field=models.EmailField(default=b'', max_length=100),
        ),
    ]
