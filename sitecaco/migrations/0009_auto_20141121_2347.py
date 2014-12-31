# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitecaco', '0008_auto_20141121_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivo',
            name='Arquivo',
            field=models.FileField(upload_to='web/'),
            preserve_default=True,
        ),
    ]
