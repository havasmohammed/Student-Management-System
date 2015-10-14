# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0023_basic_detail_emergency_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Miscellaneous_detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nss', models.BooleanField()),
                ('ncc', models.BooleanField()),
                ('sports', models.CharField(max_length=100, null=True, blank=True)),
                ('hobbies', models.CharField(max_length=100, null=True, blank=True)),
                ('personal_website', models.URLField(null=True, blank=True)),
                ('orkut_profile_url', models.URLField(null=True, blank=True)),
                ('facebook_profile_url', models.URLField(null=True, blank=True)),
                ('linkedin_profile_url', models.URLField(null=True, blank=True)),
            ],
        ),
    ]
