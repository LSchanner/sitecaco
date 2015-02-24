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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=150)),
                ('autor', models.CharField(max_length=150)),
                ('edicao', models.CharField(max_length=3)),
                ('observacao', models.CharField(blank=True, max_length=150)),
                ('disponivel', models.BooleanField(default=True)),
                ('quantidade', models.SmallIntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
