# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoOnIis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membro',
            old_name='nomeDaCongregacao',
            new_name='igreja',
        ),
        migrations.RenameField(
            model_name='membro',
            old_name='localDebaptismo',
            new_name='localDeBaptismo',
        ),
        migrations.RenameField(
            model_name='membro',
            old_name='nacionalidade',
            new_name='pais',
        ),
        migrations.AlterField(
            model_name='membro',
            name='estadoCivil',
            field=models.CharField(max_length=20),
        ),
    ]
