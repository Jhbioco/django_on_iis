# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoOnIis', '0017_auto_20150821_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diaDaSemana', models.CharField(max_length=25)),
                ('descricao', models.CharField(max_length=300)),
            ],
        ),
    ]
