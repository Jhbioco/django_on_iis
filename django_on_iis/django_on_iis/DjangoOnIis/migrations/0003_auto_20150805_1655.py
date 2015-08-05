# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoOnIis', '0002_auto_20150805_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membro',
            old_name='numeroDeIdentificao',
            new_name='numeroDeIdentificacao',
        ),
        migrations.AlterField(
            model_name='membro',
            name='foto',
            field=models.ImageField(upload_to=b'fotos/'),
        ),
    ]
