# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Pais(models.Model):
	nomeDoPais = models.CharField(max_length=50)
	def __unicode__(self):
		return unicode(self.nomeDoPais)

class Provincia(models.Model):
	nomeDaProvincia = models.CharField(max_length=50)
	idDoPais = models.ForeignKey(Pais)

	def __unicode__(self):
		return unicode(self.nomeDaProvincia)

class Municipio(models.Model):
	nomeDoMunicipio = models.CharField(max_length=50)
	idDaProvincia = models.ForeignKey(Provincia)

	def __unicode__(self):
		return unicode(self.nomeDoMunicipio)

		
class Igreja(models.Model):
	nomeDaIgreja = models.CharField(max_length=100)
	endereco = models.CharField(max_length=50)
	bairro = models.CharField(max_length=50)
	cidade = models.ForeignKey(Municipio)
	provincia = models.ForeignKey(Provincia)
	caixaPostal = models.CharField(max_length=10)
	telefone = models.CharField(max_length=20)
	email = models.EmailField(max_length=200)
	dataDeCriacao = models.DateField()
	logotipo = models.ImageField(upload_to = 'fotos/', default = 'fotos/no-img.jpg')

	def __unicode__(self):
		return unicode(self.nomeDaIgreja)



class Departamento(models.Model):
	nomeDoDepartamento = models.CharField(max_length=50)
	idDaIgreja = models.ForeignKey(Igreja)

	def __unicode__(self):
		return unicode(self.nomeDoDepartamento)



class Membro(models.Model):
	nomeDoMembro = models.CharField(max_length=100)
	estadoCivil = models.CharField(max_length=20)
	sexo = models.CharField(max_length=10)
	cargo = models.CharField(max_length=50)
	funcaoNaIgreja= models.CharField(max_length=50)
	endereco = models.CharField(max_length=50)
	bairro = models.CharField(max_length=50)
	provincia = models.ForeignKey(Provincia)
	caixaPostal = models.CharField(max_length=10)
	telefone = models.CharField(max_length=20)
	email = models.EmailField(max_length=200)
	dataDeNascimento = models.DateField()
	#naturalidade = models.ForeignKey(Municipio)
	pais = models.ForeignKey(Pais)
	grauAcademico = models.CharField(max_length=50)
	profissao = models.CharField(max_length=50)
	numeroDeIdentificacao = models.CharField(max_length=50)
	conjuge = models.CharField(max_length=100)
	filiacaoPai = models.CharField(max_length=100)
	filiacaoMae = models.CharField(max_length=100)
	dataDeConversao = models.DateField()
	procedencia = models.CharField(max_length=100)
	formaDeAdmissao = models.CharField(max_length=50)
	dataDeBaptismo = models.DateField()
	localDeBaptismo = models.CharField(max_length=50)
	dataDeConsagracaoDiacono = models.DateField()
	dataDeConsagracaoEvangelista = models.DateField()
	dataDeConsagracaoPastor = models.DateField()
	dataDeConsagracaoMissionario = models.DateField()
	departamento = models.ForeignKey(Departamento)
	igreja = models.ForeignKey(Igreja)
	numeroDeMembro= models.CharField(max_length=20)
	#foto = models.ImageField(upload_to = 'fotos/')

	def __unicode__(self):
		return unicode(self.nomeDoMembro)


class Dizimo(models.Model):
	nomeDoMembro = models.ForeignKey(Membro)
	igreja = models.ForeignKey(Igreja)
	valorDoDizimo = models.FloatField(default=None)
	dataDoDizimo = models.DateField()
	mesDoDizimo = models.CharField(max_length=20)
	anoDoDizimo=models.CharField(max_length=10)

	def __unicode__(self):
		return unicode(self.valorDoDizimo)


class Projeto(models.Model):
	igreja = models.ForeignKey(Igreja)
	descricaoDoProjeto = models.CharField(max_length=300)
	orcamento = models.FloatField(default=None)

	def __unicode__(self):
		return unicode(self.descricaoDoProjeto)


class Contribuicao(models.Model):
	nomeDoMembro = models.ForeignKey(Membro)
	igreja = models.ForeignKey(Igreja)
	valorDaContribuicao = models.FloatField(default=None)
	descricaoDaContribuicao = models.ForeignKey(Projeto)
	dataDaContribuicao = models.DateField()
	mesDaContribuicao = models.CharField(max_length=20)
	anoDaContribuicao = models.CharField(max_length=10)

	def __unicode__(self):
		return unicode(self.descricaoDaContribuicao)



class Oferta(models.Model):
	igreja = models.ForeignKey(Igreja)
	valorDaOferta = models.FloatField(default=None)
	dataDaOferta = models.DateField()
	mesDaOferta = models.CharField(max_length=20)
	anoDaOferta = models.CharField(max_length=10)

	def __unicode__(self):
		return unicode(self.valorDaOferta)




















		