# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0020_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='texto',
            field=models.CharField(default=b'vacio', max_length=300),
            preserve_default=True,
        ),
    ]
