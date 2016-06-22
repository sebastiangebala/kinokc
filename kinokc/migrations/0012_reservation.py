# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kinokc', '0011_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('imię', models.CharField(max_length=200)),
                ('nazwisko', models.CharField(max_length=200)),
                ('film', models.CharField(max_length=200)),
                ('dzień', models.DateField(blank=True, null=True)),
                ('godzina', models.TimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]
