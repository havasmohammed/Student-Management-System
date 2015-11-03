# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0039_auto_20151103_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursedetail',
            old_name='level',
            new_name='course_level',
        ),
    ]
