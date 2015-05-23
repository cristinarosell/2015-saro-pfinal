# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0013_fechaact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fechaact',
            name='fecha',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
