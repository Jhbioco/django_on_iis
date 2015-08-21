# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoOnIis', '0007_auto_20150813_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salario',
            name='salarioBase',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='salarioBase',
            field=models.FloatField(default=None),
        ),
    ]
