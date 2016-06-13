# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kinokc', '0008_remove_post_dzien_tygodnia'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='godzina',
            field=models.TimeField(default=django.utils.timezone.now, blank=True, null=True),
        ),
    ]
