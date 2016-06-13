# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kinokc', '0006_remove_post_display_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='display_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True),
        ),
    ]
