# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0027_auto_20151014_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic_detail',
            name='Class_awarded',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'FIRST CLASS WITH DISTINCTION', b'FIRST CLASS WITH DISTINCTION'), (b'FIRST CLASS', b'FIRST CLASS'), (b'SECOND CLASS', b'SECOND CLASS'), (b'PASS CLASS', b'PASS CLASS'), (b'FAIL', b'FAIL')]),
        ),
    ]
