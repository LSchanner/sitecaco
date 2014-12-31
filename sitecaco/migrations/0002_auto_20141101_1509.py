# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitecaco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagina',
            name='cartegoria',
            field=models.CharField(choices=[('Sobre', 'Sobre'), ('Serviços', 'Serviços'), ('Institucional', 'Institucional'), ('Produtos', 'Produtos'), ('Eventos', 'Eventos'), ('Livre', 'Livre')], max_length=15),
        ),
    ]
