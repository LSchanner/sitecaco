# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitecaco', '0006_arquivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to='banco_de_provas')),
                ('matéria', models.CharField(max_length=10)),
                ('semestre', models.CharField(max_length=10)),
                ('professor', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
