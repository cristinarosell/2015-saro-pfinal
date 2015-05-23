# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0017_auto_20150507_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagenbanner',
            field=models.CharField(default=b'Madrid3.jpg', max_length=32),
            preserve_default=True,
        ),
    ]
