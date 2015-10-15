# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0028_auto_20151014_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_detail',
            name='level',
            field=models.CharField(default=b'10th', max_length=4, choices=[(b'UG', b'Under Graduate'), (b'PG', b'Post Graduate'), (b'12th', b'12th'), (b'10th', b'10th')]),
        ),
    ]
