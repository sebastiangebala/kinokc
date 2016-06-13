# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinokc', '0003_remove_post_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dzien_tygodnia',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
    ]
