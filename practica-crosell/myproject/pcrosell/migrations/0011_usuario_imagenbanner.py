# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0010_auto_20150505_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagenbanner',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]
