# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0018_auto_20150515_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tamanoletra',
            field=models.CharField(default=b'small', max_length=32),
            preserve_default=True,
        ),
    ]
