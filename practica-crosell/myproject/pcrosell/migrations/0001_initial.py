# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=64)),
                ('tipo', models.CharField(max_length=32)),
                ('precio', models.FloatField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('duracion', models.DateTimeField()),
                ('largaduracion', models.BooleanField()),
                ('url', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventosUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechareg', models.DateTimeField(auto_now=True)),
                ('evento', models.ForeignKey(to='pcrosell.Evento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
                ('npag', models.CharField(max_length=32)),
                ('descrpag', models.CharField(max_length=150)),
                ('tamanoletra', models.CharField(max_length=32)),
                ('colorletra', models.CharField(max_length=32)),
                ('colorfondo', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='eventosusuario',
            name='usuario',
            field=models.ForeignKey(to='pcrosell.Usuario'),
            preserve_default=True,
        ),
    ]
