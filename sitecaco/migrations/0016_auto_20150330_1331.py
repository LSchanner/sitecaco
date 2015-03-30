# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitecaco', '0015_inscricaofisl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricaofisl',
            name='RA',
            field=models.CharField(null=True, max_length=10),
            preserve_default=True,
        ),
    ]
