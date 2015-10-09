# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0016_academic_detail_class_awarded'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_detail',
            name='stream',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
