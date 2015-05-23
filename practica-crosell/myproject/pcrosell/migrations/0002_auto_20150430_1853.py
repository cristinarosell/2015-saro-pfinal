# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='fecha',
            new_name='fechahora',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='hora',
        ),
    ]
