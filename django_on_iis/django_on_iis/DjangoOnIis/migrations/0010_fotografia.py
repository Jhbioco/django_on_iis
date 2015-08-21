# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoOnIis', '0009_auto_20150813_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeDaFoto', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to=b'fotos/%Y/%m/%d')),
            ],
        ),
    ]
