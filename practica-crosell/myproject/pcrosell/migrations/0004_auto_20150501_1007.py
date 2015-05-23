# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0003_auto_20150430_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='duracion',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
    ]
