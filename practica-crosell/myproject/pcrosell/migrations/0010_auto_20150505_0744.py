# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0009_auto_20150501_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='comentprecio',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='precio',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
