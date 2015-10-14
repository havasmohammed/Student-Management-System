# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0021_basic_detail_blood_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_detail',
            name='caste',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='basic_detail',
            name='family_income',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='basic_detail',
            name='father_profession',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='basic_detail',
            name='religion',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='basic_detail',
            name='reservation_category',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'OC', b'OC'), (b'OBC', b'OBC'), (b'MBC', b'MBC'), (b'BC', b'BC'), (b'SC', b'SC'), (b'ST', b'ST')]),
        ),
    ]
