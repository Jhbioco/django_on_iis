# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoOnIis', '0012_user_utilizador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracoes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagem1', models.ImageField(upload_to=b'fotos/%Y/%m/%d')),
                ('imagem2', models.ImageField(upload_to=b'fotos/%Y/%m/%d')),
                ('texto1', models.CharField(max_length=400)),
                ('texto2', models.CharField(max_length=400)),
                ('texto3', models.CharField(max_length=400)),
                ('texto4', models.CharField(max_length=400)),
                ('texto5', models.CharField(max_length=400)),
                ('texto6', models.CharField(max_length=400)),
                ('desenvolvedores', models.CharField(max_length=200)),
                ('igreja', models.ForeignKey(to='DjangoOnIis.Igreja')),
            ],
        ),
    ]
