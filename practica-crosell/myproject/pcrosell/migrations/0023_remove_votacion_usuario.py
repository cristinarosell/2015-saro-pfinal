# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0022_votacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votacion',
            name='usuario',
        ),
    ]
