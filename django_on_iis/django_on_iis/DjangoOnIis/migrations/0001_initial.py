# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeDoDepartamento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Igreja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeDaIgreja', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('caixaPostal', models.CharField(max_length=10)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200)),
                ('dataDeCriacao', models.DateField()),
                ('logotipo', models.ImageField(default=b'fotos/no-img.jpg', upload_to=b'fotos/')),
            ],
        ),
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeDoMembro', models.CharField(max_length=100)),
                ('estadoCivil', models.CharField(max_length=10)),
                ('sexo', models.CharField(max_length=10)),
                ('cargo', models.CharField(max_length=50)),
                ('funcaoNaIgreja', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('caixaPostal', models.CharField(max_length=10)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200)),
                ('dataDeNascimento', models.DateField()),
                ('grauAcademico', models.CharField(max_length=50)),
                ('profissao', models.CharField(max_length=50)),
                ('numeroDeIdentificao', models.CharField(max_length=50)),
                ('conjuge', models.CharField(max_length=100)),
                ('filiacaoPai', models.CharField(max_length=100)),
                ('filiacaoMae', models.CharField(max_length=100)),
                ('dataDeConversao', models.DateField()),
                ('procedencia', models.CharField(max_length=100)),
                ('formaDeAdmissao', models.CharField(max_length=50)),
                ('dataDeBaptismo', models.DateField()),
                ('localDebaptismo', models.CharField(max_length=50)),
                ('dataDeConsagracaoDiacono', models.DateField()),
                ('dataDeConsagracaoEvangelista', models.DateField()),
                ('dataDeConsagracaoPastor', models.DateField()),
                ('dataDeConsagracaoMissionario', models.DateField()),
                ('numeroDeMembro', models.CharField(max_length=20)),
                ('foto', models.ImageField(default=b'fotos/no-img.jpg', upload_to=b'fotos/')),
                ('departamento', models.ForeignKey(to='DjangoOnIis.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeDoMunicipio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeDoPais', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeDaProvincia', models.CharField(max_length=50)),
                ('idDoPais', models.ForeignKey(to='DjangoOnIis.Pais')),
            ],
        ),
        migrations.AddField(
            model_name='municipio',
            name='idDaProvincia',
            field=models.ForeignKey(to='DjangoOnIis.Provincia'),
        ),
        migrations.AddField(
            model_name='membro',
            name='nacionalidade',
            field=models.ForeignKey(to='DjangoOnIis.Pais'),
        ),
        migrations.AddField(
            model_name='membro',
            name='naturalidade',
            field=models.ForeignKey(to='DjangoOnIis.Municipio'),
        ),
        migrations.AddField(
            model_name='membro',
            name='nomeDaCongregacao',
            field=models.ForeignKey(to='DjangoOnIis.Igreja'),
        ),
        migrations.AddField(
            model_name='membro',
            name='provincia',
            field=models.ForeignKey(to='DjangoOnIis.Provincia'),
        ),
        migrations.AddField(
            model_name='igreja',
            name='cidade',
            field=models.ForeignKey(to='DjangoOnIis.Municipio'),
        ),
        migrations.AddField(
            model_name='igreja',
            name='provincia',
            field=models.ForeignKey(to='DjangoOnIis.Provincia'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='idDaIgreja',
            field=models.ForeignKey(to='DjangoOnIis.Igreja'),
        ),
    ]
