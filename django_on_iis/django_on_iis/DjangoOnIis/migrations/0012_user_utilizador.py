# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoOnIis', '0011_auto_20150814_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userEmail', models.EmailField(max_length=100)),
                ('userPassword', models.CharField(max_length=100)),
                ('funcionario', models.ForeignKey(to='DjangoOnIis.Funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Utilizador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('nomeDoMembro', models.ForeignKey(to='DjangoOnIis.Membro')),
            ],
        ),
    ]
