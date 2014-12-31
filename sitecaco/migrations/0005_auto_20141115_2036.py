# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitecaco', '0004_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='title',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
    ]
