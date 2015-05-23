# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0002_auto_20150430_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fechahora',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
