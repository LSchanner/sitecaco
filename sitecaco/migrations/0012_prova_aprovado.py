# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitecaco', '0011_auto_20141226_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='prova',
            name='aprovado',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
