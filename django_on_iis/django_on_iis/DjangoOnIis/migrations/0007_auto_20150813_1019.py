# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoOnIis', '0006_auto_20150811_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeDoFuncionario', models.CharField(max_length=100)),
                ('estadoCivil', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=10)),
                ('cargo', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('caixaPostal', models.CharField(max_length=10)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200)),
                ('dataDeNascimento', models.DateField()),
                ('grauAcademico', models.CharField(max_length=50)),
                ('profissao', models.CharField(max_length=50)),
                ('numeroDeIdentificacao', models.CharField(max_length=50)),
                ('filiacaoPai', models.CharField(max_length=100)),
                ('filiacaoMae', models.CharField(max_length=100)),
                ('numeroDeFuncionario', models.CharField(max_length=20)),
                ('pais', models.ForeignKey(to='DjangoOnIis.Pais')),
                ('provincia', models.ForeignKey(to='DjangoOnIis.Provincia')),
            ],
        ),
        migrations.CreateModel(
            name='Salario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('salarioAno', models.CharField(max_length=10)),
                ('salarioMes', models.CharField(max_length=20)),
                ('salarioBase', models.FloatField(default=None)),
                ('salarioSS', models.FloatField(default=None)),
                ('salarioIRT', models.FloatField(default=None)),
                ('salarioNumerodeFaltas', models.CharField(max_length=5)),
                ('salarioBonus', models.CharField(max_length=100)),
                ('salarioLiquido', models.FloatField(default=None)),
                ('nomeDoFuncionario', models.ForeignKey(to='DjangoOnIis.Funcionario')),
            ],
        ),
        migrations.RenameField(
            model_name='contribuicao',
            old_name='nomeDomembro',
            new_name='nomeDoMembro',
        ),
        migrations.RenameField(
            model_name='dizimo',
            old_name='nomeDomembro',
            new_name='nomeDoMembro',
        ),
    ]
