# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0015_auto_20150507_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fechahora',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventosusuario',
            name='fechareg',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fechaact',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
