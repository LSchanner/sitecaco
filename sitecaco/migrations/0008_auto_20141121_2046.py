# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitecaco', '0007_prova'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prova',
            old_name='matéria',
            new_name='materia',
        ),
    ]
