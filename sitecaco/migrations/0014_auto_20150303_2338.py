# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitecaco', '0013_livro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='observacao',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
