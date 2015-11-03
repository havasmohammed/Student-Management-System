# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0040_auto_20151103_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicdetail',
            name='cname',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='academicdetail',
            name='history_of_arrears',
            field=models.TextField(default=b'', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='academicdetail',
            name='hsc_major',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='academicdetail',
            name='hsc_passed_out_year',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=0, blank=True),
        ),
        migrations.AddField(
            model_name='academicdetail',
            name='hsc_percentage',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='academicdetail',
            name='tenth_passed_out_year',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=0, blank=True),
        ),
        migrations.AddField(
            model_name='academicdetail',
            name='tenth_percentage',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='basicdetail',
            name='DOB',
            field=models.DateField(help_text=b'What is your date of birth as per records?', null=True, blank=True),
        ),
    ]
