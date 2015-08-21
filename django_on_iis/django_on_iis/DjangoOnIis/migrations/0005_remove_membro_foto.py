# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoOnIis', '0004_remove_membro_naturalidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membro',
            name='foto',
        ),
    ]
