# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0008_auto_20150501_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='descripcion',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='identif',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
