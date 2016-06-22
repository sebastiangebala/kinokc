# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kinokc', '0012_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='ilość_biletów',
            field=models.CharField(max_length=200, default=datetime.datetime(2016, 6, 19, 16, 51, 33, 730764, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
