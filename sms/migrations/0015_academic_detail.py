# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0014_basic_detail_id_card_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Attendence_percentage', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('First_year_percentage_of_marks', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('Second_year_percentage_of_marks', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('Third_year_percentage_of_marks', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('Fourth_year_percentage_of_marks', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('Total_percentage_of_marks', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
            ],
        ),
    ]
