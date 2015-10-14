# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0026_remove_basic_detail_id_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic_detail',
            name='Class_awarded',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'FIRST CLASS WITH DISTINCTION', b'FIRST CLASS WITH DISTINCTION'), (b'FIRST CLASS', b'FIRST CLASS'), (b'SECOND CLASS', b'SECONd CLASS'), (b'PASS CLASS', b'PASS CLASS'), (b'FAIL', b'FAIL')]),
        ),
    ]
