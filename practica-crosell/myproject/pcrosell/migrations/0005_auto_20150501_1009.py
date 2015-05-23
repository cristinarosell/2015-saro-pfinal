# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0004_auto_20150501_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='duracion',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
