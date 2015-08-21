# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoOnIis', '0005_remove_membro_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribuicao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valorDaContribuicao', models.FloatField(default=None)),
                ('dataDaContribuicao', models.DateField()),
                ('mesDaContribuicao', models.CharField(max_length=20)),
                ('anoDaContribuicao', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Dizimo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valorDoDizimo', models.FloatField(default=None)),
                ('dataDoDizimo', models.DateField()),
                ('mesDoDizimo', models.CharField(max_length=20)),
                ('anoDoDizimo', models.CharField(max_length=10)),
                ('igreja', models.ForeignKey(to='DjangoOnIis.Igreja')),
                ('nomeDomembro', models.ForeignKey(to='DjangoOnIis.Membro')),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valorDaOferta', models.FloatField(default=None)),
                ('dataDaOferta', models.DateField()),
                ('mesDaOferta', models.CharField(max_length=20)),
                ('anoDaOferta', models.CharField(max_length=10)),
                ('igreja', models.ForeignKey(to='DjangoOnIis.Igreja')),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricaoDoProjeto', models.CharField(max_length=300)),
                ('orcamento', models.FloatField(default=None)),
                ('igreja', models.ForeignKey(to='DjangoOnIis.Igreja')),
            ],
        ),
        migrations.AddField(
            model_name='contribuicao',
            name='descricaoDaContribuicao',
            field=models.ForeignKey(to='DjangoOnIis.Projeto'),
        ),
        migrations.AddField(
            model_name='contribuicao',
            name='igreja',
            field=models.ForeignKey(to='DjangoOnIis.Igreja'),
        ),
        migrations.AddField(
            model_name='contribuicao',
            name='nomeDomembro',
            field=models.ForeignKey(to='DjangoOnIis.Membro'),
        ),
    ]
