# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinokc', '0009_post_godzina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='display_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
