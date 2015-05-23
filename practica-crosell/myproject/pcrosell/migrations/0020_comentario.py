# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrosell', '0019_auto_20150515_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechacom', models.DateTimeField()),
                ('evento', models.ForeignKey(to='pcrosell.Evento')),
                ('usuario', models.ForeignKey(to='pcrosell.Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
