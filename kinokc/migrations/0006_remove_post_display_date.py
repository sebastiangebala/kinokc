# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinokc', '0005_auto_20160601_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='display_date',
        ),
    ]
