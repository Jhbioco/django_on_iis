# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoOnIis', '0014_auto_20150821_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='dataDeBaptismo',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='membro',
            name='dataDeConsagracaoDiacono',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='membro',
            name='dataDeConsagracaoEvangelista',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='membro',
            name='dataDeConsagracaoMissionario',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='membro',
            name='dataDeConsagracaoPastor',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='membro',
            name='dataDeConversao',
            field=models.DateField(null=True),
        ),
    ]
