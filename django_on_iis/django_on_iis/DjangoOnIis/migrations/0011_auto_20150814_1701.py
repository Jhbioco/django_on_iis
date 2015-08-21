# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoOnIis', '0010_fotografia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('autor', models.CharField(max_length=100)),
                ('comentario', models.CharField(max_length=5000)),
                ('data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=50)),
                ('numeroDeSerie', models.CharField(max_length=30)),
                ('dataDaAquisicao', models.DateField()),
                ('modelo', models.CharField(max_length=30)),
                ('localizacao', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=30)),
                ('preco', models.FloatField(default=None)),
                ('obs', models.CharField(max_length=300)),
                ('igreja', models.ForeignKey(to='DjangoOnIis.Igreja')),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evento', models.CharField(max_length=5000)),
                ('dataDoEvento', models.DateField()),
                ('localDoEvento', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('dataDaPublicacao', models.DateField()),
                ('departamento', models.ForeignKey(to='DjangoOnIis.Departamento')),
                ('igreja', models.ForeignKey(to='DjangoOnIis.Igreja')),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=300)),
                ('noticia', models.CharField(max_length=5000)),
                ('foto', models.ImageField(upload_to=b'fotos/%Y/%m/%d')),
                ('dataPublicacao', models.DateField()),
                ('tipo', models.CharField(max_length=20)),
                ('funcionario', models.ForeignKey(to='DjangoOnIis.Membro')),
            ],
        ),
        migrations.DeleteModel(
            name='Fotografia',
        ),
        migrations.AddField(
            model_name='comentarios',
            name='noticia',
            field=models.ForeignKey(to='DjangoOnIis.Noticias'),
        ),
    ]
