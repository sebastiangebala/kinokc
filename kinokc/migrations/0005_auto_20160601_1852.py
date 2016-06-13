# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kinokc', '0004_post_dzien_tygodnia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='display_date',
            field=models.DateTimeField(null=True, default=django.utils.timezone.now, blank=True),
        ),
    ]
