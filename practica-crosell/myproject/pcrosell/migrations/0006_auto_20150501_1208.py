# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0005_auto_20150501_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='precio',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
    ]
