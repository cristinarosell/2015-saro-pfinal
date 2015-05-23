# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0021_comentario_texto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('puntuacion', models.IntegerField()),
                ('evento', models.ForeignKey(to='pcrosell.Evento')),
                ('usuario', models.ForeignKey(to='pcrosell.Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
