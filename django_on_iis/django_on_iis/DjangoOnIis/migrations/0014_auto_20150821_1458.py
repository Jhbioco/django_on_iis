# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoOnIis', '0013_configuracoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='dataDeBaptismo',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='membro',
            name='dataDeConsagracaoDiacono',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='membro',
            name='dataDeConsagracaoEvangelista',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='membro',
            name='dataDeConsagracaoMissionario',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='membro',
            name='dataDeConsagracaoPastor',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='membro',
            name='dataDeConversao',
            field=models.DateField(blank=True),
        ),
    ]
