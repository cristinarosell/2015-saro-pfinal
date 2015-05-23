# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0011_usuario_imagenbanner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='colorfondo',
            field=models.CharField(default=b'white', max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='colorletra',
            field=models.CharField(default=b'black', max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='descrpag',
            field=models.CharField(default=b'vacio', max_length=150),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='imagenbanner',
            field=models.CharField(default=b'img.png', max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tamanoletra',
            field=models.CharField(default=b'medium', max_length=32),
            preserve_default=True,
        ),
    ]
