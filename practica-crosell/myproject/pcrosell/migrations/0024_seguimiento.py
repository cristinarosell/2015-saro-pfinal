# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0023_remove_votacion_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario', models.ForeignKey(to='pcrosell.Usuario')),
                ('usuarioseguido', models.ForeignKey(related_name='seguido', to='pcrosell.Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
