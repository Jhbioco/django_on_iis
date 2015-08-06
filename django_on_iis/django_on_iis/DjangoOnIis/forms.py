#!/usr/bin/python
# -*- coding: latin-1 -*-

from django import forms
from .models import Igreja,Pais,Provincia,Municipio,Departamento,Membro
from django import forms
from .models import Pais, Provincia, Municipio, Igreja, Departamento, Membro
from django.db import connection

def dictfetchall(cursor):
	desc = cursor.description
	return [dict(zip([call[0] for call in desc],raw)) for raw in cursor.fetchall()]

def get_provincia():
	provincia_opcao = connection.cursor()
	provincia_opcao.execute("select nomeDaProvincia, id from DjangoOnIis_provincia");
	return provincia_opcao.fetchall()

def get_pais():
	pais_opcao = connection.cursor()
	pais_opcao.execute("select nomeDoPais,nomeDoPais from DjangoOnIis_pais");
	return pais_opcao.fetchall()


def get_departamento():
	departamento_opcao = connection.cursor()
	departamento_opcao.execute("select nomeDoDepartamento,nomeDoDepartamento from DjangoOnIis_departamento");
	return departamento_opcao.fetchall()


def get_igreja():
	igreja_opcao = connection.cursor()
	igreja_opcao.execute("select nomeDaIgreja, provincia_id from DjangoOnIis_igreja");
	return igreja_opcao.fetchall()

class MembroForm(forms.Form):
	
	nomeDoMembro = forms.CharField(max_length=100)
	estadoCivil = forms.CharField(max_length=20)
	sexo = forms.CharField(max_length=10)
	cargo = forms.CharField(max_length=50)
	funcaoNaIgreja = forms.CharField(max_length=50)
	endereco = forms.CharField(max_length=50)
	bairro = forms.CharField(max_length=50)
	provincia = forms.ChoiceField(choices=get_provincia(),required=False)
	caixaPostal = forms.CharField(max_length=10)
	telefone = forms.CharField(max_length=20)
	email = forms.EmailField(max_length=200)
	dataDeNascimento = forms.DateField()
	pais = forms.ChoiceField(choices=get_pais())
	grauAcademico = forms.CharField(max_length=50)
	profissao = forms.CharField(max_length=50)
	numeroDeIdentificacao = forms.CharField(max_length=50)
	conjuge = forms.CharField(max_length=100)
	filiacaoPai = forms.CharField(max_length=100)
	filiacaoMae = forms.CharField(max_length=100)
	dataDeConversao = forms.DateField()
	procedencia = forms.CharField(max_length=100)
	formaDeAdmissao = forms.CharField(max_length=50)
	dataDeBaptismo = forms.DateField()
	localDeBaptismo = forms.CharField(max_length=50,required=False)
	dataDeConsagracaoDiacono = forms.DateField()
	dataDeConsagracaoEvangelista = forms.DateField()
	dataDeConsagracaoPastor = forms.DateField()
	dataDeConsagracaoMissionario = forms.DateField()
	departamento = forms.ChoiceField(choices=get_departamento())
	igreja = forms.ChoiceField(choices=get_igreja())
	numeroDeMembro = forms.CharField(max_length=20)
	foto = forms.ImageField(required=False)