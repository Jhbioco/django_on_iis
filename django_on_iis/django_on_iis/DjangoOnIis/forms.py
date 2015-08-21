#!/usr/bin/python
# -*- coding: latin-1 -*-

from django import forms
from django import forms
from .models import Pais, Provincia, Municipio, Igreja, Departamento, Membro, Oferta, Projeto, Dizimo, Contribuicao, Salario, Funcionario, Equipamento, Noticias,Comentarios,Eventos, Utilizador, Configuracoes 
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
	localDeBaptismo = forms.CharField(max_length=50,required=True)
	dataDeConsagracaoDiacono = forms.DateField()
	dataDeConsagracaoEvangelista = forms.DateField()
	dataDeConsagracaoPastor = forms.DateField()
	dataDeConsagracaoMissionario = forms.DateField()
	departamento = forms.ChoiceField(choices=get_departamento())
	igreja = forms.ChoiceField(choices=get_igreja())
	numeroDeMembro = forms.CharField(max_length=20)
	#foto = forms.ImageField(required=False)

class DizimoForm(forms.Form):
	nomeDoMembro = forms.CharField(required=False)
	igreja = forms.CharField()
	valorDoDizimo = forms.FloatField()
	dataDoDizimo = forms.DateField()
	mesDoDizimo = forms.CharField()
	anoDoDizimo = forms.CharField()

class ContribuicaoForm(forms.Form):
	nomeDoMembro = forms.CharField()
	igreja = forms.CharField()
	valorDaContribuicao = forms.FloatField()
	descricaoDaContribuicao = forms.CharField()
	dataDaContribuicao = forms.DateField()
	mesDaContribuicao = forms.CharField()
	anoDaContribuicao = forms.CharField()

class OfertaForm(forms.Form):
	igreja = forms.CharField()
	valorDaOferta = forms.FloatField()
	dataDaOferta = forms.DateField()
	mesDaOferta = forms.CharField()
	anoDaOferta = forms.CharField()


class ProjetoForm(forms.Form):
	igreja = forms.CharField()
	descricaoDoProjeto = forms.CharField()
	orcamento = forms.FloatField()


class FuncionarioForm(forms.Form):
	nomeDoFuncionario = forms.CharField(max_length=100)
	estadoCivil = forms.CharField(max_length=20)
	sexo = forms.CharField(max_length=10)
	cargo = forms.CharField(max_length=50)
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
	filiacaoPai = forms.CharField(max_length=100)
	filiacaoMae = forms.CharField(max_length=100)
	numeroDeFuncionario = forms.CharField(max_length=20)
	salarioBase = forms.FloatField()
	#foto = forms.ImageField(required=False)


class SalarioForm(forms.Form):
	nomeDoFuncionario=forms.CharField()
	salarioAno = forms.CharField()
	salarioMes= forms.CharField()
	salarioSS = forms.FloatField()
	salarioIRT = forms.FloatField()
	salarioNumerodeFaltas = forms.CharField()
	salarioBonus = forms.FloatField()
	salarioLiquido = forms.FloatField()

class EquipamentoForm(forms.Form):
    igreja = forms.CharField()
    nome=forms.CharField()
    marca = forms.CharField()
    numeroDeSerie = forms.CharField()
    dataDaAquisicao = forms.DateField()
    modelo = forms.CharField()
    localizacao = forms.CharField()
    estado = forms.CharField()
    preco = forms.FloatField()
    obs = forms.CharField()

class NoticiasForm(forms.Form):
    titulo = forms.CharField()
    noticia=forms.CharField()
    foto = forms.ImageField(label='Seleccionar imagem')
    funcionario=forms.CharField()
    dataPublicacao = forms.DateField()
    tipo = forms.CharField(required=False)


class ComentariosForm(forms.Form):
    noticia=forms.CharField()
    autor = forms.CharField()
    comentario = forms.CharField()
    data = forms.DateField()
    


class EventosForm(forms.Form):
    departamento = forms.CharField()
    evento = forms.CharField()
    dataDoEvento = forms.DateField()
    localDoEvento = forms.CharField()
    igreja= forms.CharField()
    autor = forms.CharField()
    dataDaPublicacao = forms.DateField()



class ConfiguracoesForm(forms.Form):
	igreja= forms.CharField()
	imagem1 = forms.ImageField(label='Seleccionar imagem')
	imagem2 = forms.ImageField(label='Seleccionar imagem')
	texto1 = forms.CharField()
	texto2 = forms.CharField()
	texto3 = forms.CharField()
	texto4 = forms.CharField()
	texto5 = forms.CharField()
	texto6 = forms.CharField()
	desenvolvedores = forms.CharField()



class UserForm(forms.Form):
	funcionario = forms.ChoiceField()
	userEmail = forms.ChoiceField()
	Userpassword = forms.ChoiceField()




