# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0029_auto_20151015_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicDetail',
            fields=[
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(default=b'', max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('sid', models.IntegerField(serialize=False, primary_key=True)),
                ('gender', models.CharField(default=b'M', max_length=2, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('address', models.CharField(max_length=200)),
                ('DOB', models.DateField()),
                ('father_name', models.CharField(default=b'', max_length=200)),
                ('mother_name', models.CharField(default=b'', max_length=200)),
                ('email', models.EmailField(default=b'', max_length=100)),
                ('blood_group', models.CharField(blank=True, max_length=4, null=True, choices=[(b'O+', b'O+'), (b'O-', b'O-'), (b'A+', b'A+'), (b'A-', b'A-'), (b'B+', b'B+'), (b'B-', b'B-'), (b'AB+', b'AB+'), (b'AB-', b'AB-')])),
                ('father_profession', models.CharField(max_length=100, null=True, blank=True)),
                ('family_income', models.IntegerField(null=True, blank=True)),
                ('religion', models.CharField(max_length=30, null=True, blank=True)),
                ('caste', models.CharField(max_length=30, null=True, blank=True)),
                ('reservation_category', models.CharField(blank=True, max_length=10, null=True, choices=[(b'OC', b'OC'), (b'OBC', b'OBC'), (b'MBC', b'MBC'), (b'BC', b'BC'), (b'SC', b'SC'), (b'ST', b'ST')])),
                ('emergency_contact_number', models.CharField(max_length=20, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cname', models.CharField(unique=True, max_length=50)),
                ('stream', models.CharField(default=b'', max_length=50)),
                ('code', models.CharField(default=b'', help_text=b'Code of the stream', unique=True, max_length=10)),
                ('year_of_registration', models.BigIntegerField()),
                ('duration', models.IntegerField(default=2, help_text=b'Duration of the course in years')),
                ('level', models.CharField(default=b'10th', max_length=4, choices=[(b'UG', b'Under Graduate'), (b'PG', b'Post Graduate'), (b'12th', b'12th'), (b'10th', b'10th')])),
            ],
        ),
        migrations.RenameModel(
            old_name='Academic_detail',
            new_name='AcademicDetail',
        ),
        migrations.RenameModel(
            old_name='Login_page',
            new_name='LoginPage',
        ),
        migrations.RenameModel(
            old_name='Miscellaneous_detail',
            new_name='MiscellaneousDetail',
        ),
        migrations.DeleteModel(
            name='Basic_detail',
        ),
        migrations.DeleteModel(
            name='Course_detail',
        ),
    ]
