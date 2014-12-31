# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitecaco', '0002_auto_20141101_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pagina',
            name='cartegoria',
            field=models.CharField(max_length=15, choices=[('Serviços', 'Serviços'), ('Institucional', 'Institucional'), ('Eventos', 'Eventos'), ('Livre', 'Livre')]),
        ),
    ]
