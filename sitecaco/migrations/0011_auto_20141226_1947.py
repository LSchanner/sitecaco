# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sitecaco.models


class Migration(migrations.Migration):

    dependencies = [
        ('sitecaco', '0010_auto_20141122_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prova',
            name='file',
            field=models.FileField(upload_to=sitecaco.models.nomedoarquivo),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prova',
            name='semestre',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
