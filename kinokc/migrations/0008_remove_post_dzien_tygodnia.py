# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinokc', '0007_post_display_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dzien_tygodnia',
        ),
    ]
