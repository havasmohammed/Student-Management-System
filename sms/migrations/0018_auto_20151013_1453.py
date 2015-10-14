# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0017_course_detail_stream'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_detail',
            name='cnum',
        ),
        migrations.RemoveField(
            model_name='course_detail',
            name='credits',
        ),
        migrations.AddField(
            model_name='course_detail',
            name='code',
            field=models.CharField(default=b'', unique=True, max_length=10),
        ),
        migrations.AddField(
            model_name='course_detail',
            name='duration',
            field=models.IntegerField(default=2, help_text=b'Duration of the course in years'),
        ),
        migrations.AddField(
            model_name='course_detail',
            name='level',
            field=models.CharField(default=b'UG', max_length=4, choices=[(b'UG', b'Under Graduate'), (b'PG', b'Post Graduate')]),
        ),
        migrations.AlterField(
            model_name='course_detail',
            name='cname',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
