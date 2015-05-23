# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0007_auto_20150501_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='precio',
            field=models.CharField(max_length=64),
            preserve_default=True,
        ),
    ]
