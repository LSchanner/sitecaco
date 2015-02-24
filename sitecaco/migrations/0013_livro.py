# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitecaco', '0012_prova_aprovado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('autor', models.CharField(max_length=150)),
                ('edicao', models.CharField(max_length=50)),
                ('observacao', models.TextField()),
                ('disponivel', models.BooleanField(default=True)),
                ('quantidade', models.SmallIntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
