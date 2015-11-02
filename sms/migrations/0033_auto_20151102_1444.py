# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0032_auto_20151030_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academicdetail',
            old_name='Attendence_percentage',
            new_name='attendence_percentage',
        ),
        migrations.RenameField(
            model_name='academicdetail',
            old_name='Class_awarded',
            new_name='class_awarded',
        ),
        migrations.RenameField(
            model_name='academicdetail',
            old_name='First_year_percentage_of_marks',
            new_name='first_year_percentage_of_marks',
        ),
        migrations.RenameField(
            model_name='academicdetail',
            old_name='Fourth_year_percentage_of_marks',
            new_name='fourth_year_percentage_of_marks',
        ),
        migrations.RenameField(
            model_name='academicdetail',
            old_name='Second_year_percentage_of_marks',
            new_name='second_year_percentage_of_marks',
        ),
        migrations.RenameField(
            model_name='academicdetail',
            old_name='Third_year_percentage_of_marks',
            new_name='third_year_percentage_of_marks',
        ),
        migrations.RenameField(
            model_name='academicdetail',
            old_name='Total_percentage_of_marks',
            new_name='total_percentage_of_marks',
        ),
    ]
