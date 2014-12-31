# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ata',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ('-time',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ('time',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'ordering': ('-time',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('flatpage_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='flatpages.FlatPage')),
                ('cartegoria', models.IntegerField(choices=[(1, 'Sobre'), (2, 'Serviços'), (3, 'Institucional'), (4, 'Livre')])),
                ('banner', models.ImageField(upload_to='', blank=True)),
            ],
            options={
            },
            bases=('flatpages.flatpage',),
        ),
        migrations.AddField(
            model_name='comentario',
            name='noticia',
            field=models.ForeignKey(to='sitecaco.Noticia'),
            preserve_default=True,
        ),
    ]
