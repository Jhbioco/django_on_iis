# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoOnIis', '0016_auto_20150821_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'fotos/%Y/%m/%d', blank=True),
        ),
        migrations.AddField(
            model_name='membro',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'fotos/%Y/%m/%d', blank=True),
        ),
    ]
