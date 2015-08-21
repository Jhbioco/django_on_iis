# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoOnIis', '0008_auto_20150813_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salario',
            name='salarioBonus',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='salario',
            name='salarioNumerodeFaltas',
            field=models.CharField(max_length=10),
        ),
    ]
