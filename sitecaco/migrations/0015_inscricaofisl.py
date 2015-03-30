# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitecaco', '0014_auto_20150303_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='InscricaoFISL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('sexo', models.CharField(max_length=150, choices=[('M', 'M'), ('F', 'F')])),
                ('RA', models.CharField(max_length=10)),
                ('nascimento', models.DateField()),
                ('cidade', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=20)),
                ('RG', models.CharField(max_length=20)),
                ('Orgao_expedidor', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=30)),
                ('vinculo', models.CharField(max_length=50, choices=[('Computeiro', 'Aluno Computação Unicamp'), ('Unicamper não Computeiro', 'Aluno Unicamp'), ('Brother X', 'Nenhum/Outro')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
