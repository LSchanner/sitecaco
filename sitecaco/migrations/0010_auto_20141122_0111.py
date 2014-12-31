# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitecaco', '0009_auto_20141121_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prova',
            name='professor',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prova',
            name='semestre',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
