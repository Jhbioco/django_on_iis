# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :
from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
from .models import Pais,Provincia,Programa, Municipio, Igreja, Departamento, Membro,Dizimo,Contribuicao,Oferta,Projeto, Funcionario, Salario, User
#from .forms import IgrejaForm
from django.db import connection
from .forms import MembroForm,DizimoForm,ProgramaForm,ContribuicaoForm,ProjetoForm,OfertaForm, FuncionarioForm, SalarioForm, UserForm, PesquisarNoticiaForm

from .forms import EquipamentoForm
from .models import Equipamento
from .forms import NoticiasForm,EventosForm,ComentariosForm
from .models import Noticias,Eventos,Comentarios
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.pagesizes import landscape
import sys 
import time, datetime

reload(sys)  
sys.setdefaultencoding('utf8')

# View para inserir membros

def dictfetchall(cursor):
	desc = cursor.description
	return [dict(zip([call[0] for call in desc],raw)) for raw in cursor.fetchall()]

def provincia_pesquisa(opcao):
	provincia_opcao = connection.cursor()
	provincia_opcao.execute("select distinct (id) from DjangoOnIis_provincia where nomeDaProvincia='%s'" % opcao);
	return dictfetchall(provincia_opcao)

def lista_provincia():
	provincia_opcao = connection.cursor()
	provincia_opcao.execute("select distinct (id),nomeDaProvincia from DjangoOnIis_provincia");
	return dictfetchall(provincia_opcao)



def lista_pais():
	pais_opcao= connection.cursor()
	pais_opcao.execute("select nomeDoPais from DjangoOnIis_pais ");
	return dictfetchall(pais_opcao)


"""def inserirMembro(request):
	provincia = lista_provincia()
	pais = lista_pais
	departamento=Departamento.objects.all()
	igreja = Igreja.objects.all()

	return render(request, 'inserirMembros.html',{'provincia':provincia,'pais':pais,'departamento':departamento,'igreja':igreja})"""

def home(request):
	dados = {}
	template = 'home.html'
	return render(request,template,dados)

def homeMembro(request):


	if request.method == 'POST':
		form = MembroForm(request.POST , request.FILES)
		if form.is_valid():
			provincia = Provincia.objects.get(nomeDaProvincia=form.cleaned_data['provincia'])
			pais = Pais.objects.get(nomeDoPais=form.cleaned_data['pais'])
			departamento = Departamento.objects.get(nomeDoDepartamento=form.cleaned_data['departamento'])
			igreja = Igreja.objects.get(nomeDaIgreja=form.cleaned_data['igreja'])
			nomeDoMembro = form.cleaned_data['nomeDoMembro']
			estadoCivil = form.cleaned_data['estadoCivil']
			sexo = form.cleaned_data['sexo']
			cargo = form.cleaned_data['cargo']
			funcaoNaIgreja = form.cleaned_data['funcaoNaIgreja']
			endereco = form.cleaned_data['endereco']
			bairro = form.cleaned_data['bairro']
			caixaPostal = form.cleaned_data['caixaPostal']
			telefone = form.cleaned_data['telefone']
			email = form.cleaned_data['email']
			dataDeNascimento = form.cleaned_data['dataDeNascimento']
			grauAcademico = form.cleaned_data['grauAcademico']
			profissao = form.cleaned_data['profissao']
			numeroDeIdentificacao = form.cleaned_data['numeroDeIdentificacao']
			conjuge = form.cleaned_data['conjuge']
			filiacaoPai = form.cleaned_data['filiacaoPai']
			filiacaoMae = form.cleaned_data['filiacaoMae']
			dataDeConversao = form.cleaned_data['dataDeConversao']
			procedencia = form.cleaned_data['procedencia']
			formaDeAdmissao = form.cleaned_data['formaDeAdmissao']
			dataDeBaptismo = form.cleaned_data['dataDeBaptismo']
			localDeBaptismo = form.cleaned_data['localDeBaptismo']
			dataDeConsagracaoDiacono = form.cleaned_data['dataDeConsagracaoDiacono']
			dataDeConsagracaoEvangelista = form.cleaned_data['dataDeConsagracaoEvangelista']
			dataDeConsagracaoPastor = form.cleaned_data['dataDeConsagracaoPastor']
			dataDeConsagracaoMissionario = form.cleaned_data['dataDeConsagracaoMissionario']
			numeroDeMembro = form.cleaned_data['numeroDeMembro']
			

			new_membro=Membro(nomeDoMembro=nomeDoMembro, estadoCivil=estadoCivil, sexo=sexo,
				cargo = cargo, funcaoNaIgreja=funcaoNaIgreja, endereco=endereco, bairro=bairro, provincia=provincia, caixaPostal=caixaPostal,
				telefone=telefone, email=email, dataDeNascimento=dataDeNascimento, pais=pais, grauAcademico=grauAcademico,
				profissao=profissao, numeroDeIdentificacao=numeroDeIdentificacao, conjuge=conjuge, filiacaoPai=filiacaoPai,
				filiacaoMae=filiacaoMae, dataDeConversao=dataDeConversao, procedencia=procedencia, formaDeAdmissao= formaDeAdmissao,
				dataDeBaptismo=dataDeBaptismo, localDeBaptismo=localDeBaptismo, dataDeConsagracaoDiacono= dataDeConsagracaoDiacono,
				dataDeConsagracaoEvangelista= dataDeConsagracaoEvangelista, dataDeConsagracaoPastor=dataDeConsagracaoPastor,
				dataDeConsagracaoMissionario=dataDeConsagracaoMissionario, departamento=departamento,igreja=igreja,
				numeroDeMembro=numeroDeMembro,foto=request.FILES['foto'])
			salvar=new_membro.save()
	else:
		form = MembroForm()

	provincia = Provincia.objects.all()
	pais = Pais.objects.all()
	departamento=Departamento.objects.all()
	igreja = Igreja.objects.all()

	return render(request, 'homeMembro.html',{'form':form,'provincia':provincia,'pais':pais,'departamento':departamento,'igreja':igreja})



#Queries 

def get_nome(informacao):
	query=connection.cursor()
	query.execute("select DjangoOnIis_membro.id, nomeDoMembro, numeroDeMembro, estadoCivil, sexo, funcaoNaIgreja, telefone,DjangoOnIis_departamento.nomeDoDepartamento from DjangoOnIis_membro, DjangoOnIis_departamento where nomeDoMembro like %s ",("%" + informacao +"%",));
	return dictfetchall(query)

def get_numero_membro(informacao):
	query=connection.cursor()
	query.execute("select DjangoOnIis_membro.id, nomeDoMembro, numeroDeMembro, estadoCivil, sexo, funcaoNaIgreja, telefone,DjangoOnIis_departamento.nomeDoDepartamento from DjangoOnIis_membro, DjangoOnIis_departamento where numeroDeMembro like %s ", ("%" + informacao + "%",));
	return dictfetchall(query)

def get_profissao_membro(informacao):
	query=connection.cursor()
	query.execute("select DjangoOnIis_membro.id, nomeDoMembro, numeroDeMembro, estadoCivil, sexo, funcaoNaIgreja, telefone,DjangoOnIis_departamento.nomeDoDepartamento from DjangoOnIis_membro, DjangoOnIis_departamento where profissao like %s ", ("%" + informacao + "%",));
	return dictfetchall(query)

def get_funcao_membro(informacao):
	query=connection.cursor()
	query.execute("select DjangoOnIis_membro.id, nomeDoMembro, numeroDeMembro, estadoCivil, sexo, funcaoNaIgreja, telefone,DjangoOnIis_departamento.nomeDoDepartamento from DjangoOnIis_membro, DjangoOnIis_departamento where funcaoNaIgreja like %s ", ("%" + informacao + "%",));
	return dictfetchall(query)

def get_grau_membro(informacao):
	query=connection.cursor()
	query.execute("select DjangoOnIis_membro.id, nomeDoMembro, numeroDeMembro, estadoCivil, sexo, funcaoNaIgreja, telefone,DjangoOnIis_departamento.nomeDoDepartamento from DjangoOnIis_membro, DjangoOnIis_departamento where grauAcademico = '%s' " %informacao);
	return dictfetchall(query)
def get_todos(informacao):
	query=connection.cursor()
	query.execute("select DjangoOnIis_membro.id, nomeDoMembro, numeroDeMembro, estadoCivil, sexo, funcaoNaIgreja, telefone,DjangoOnIis_departamento.nomeDoDepartamento from DjangoOnIis_membro, DjangoOnIis_departamento");
	return dictfetchall(query)

def get_editar_membro(valor):
	query = connection.cursor()
	query.execute("select * from DjangoOnIis_membro where id = '%s'" % valor);
	return dictfetchall(query)

def removerMembro(valor):
	query = connection.cursor()
	query.execute("delete from DjangoOnIis_membro where id = '%s'" % valor);
	return dictfetchall(query)

def pesquisarDizimo(valor, ano):
	query = connection.cursor()
	query.execute("select * from DjangoOnIis_dizimo where nomeDomembro_id = '%s' and anoDoDizimo = '%s'" %(valor, ano)) ;
	return dictfetchall(query)

def pesquisarDizimoTodos(valor):
	query = connection.cursor()
	query.execute("select * from DjangoOnIis_dizimo where nomeDomembro_id = '%s'" %valor);
	return dictfetchall(query)

def pesquisarContribuicao(valor, ano):
	query = connection.cursor()
	query.execute("select * from DjangoOnIis_contribuicao where nomeDomembro_id = '%s' and anoDaContribuicao = '%s'" %(valor, ano)) ;
	return dictfetchall(query)

def pesquisarContribuicaoTodos(valor):
	query = connection.cursor()
	query.execute("select * from DjangoOnIis_contribuicao where nomeDomembro_id = '%s'" %valor);
	return dictfetchall(query)


def totalAno(ano):
	query = connection.cursor()
	query.execute("select sum(valorDoDizimo) as totalDizimo,anoDoDizimo, mesDoDizimo, dataDoDizimo from DjangoOnIis_dizimo where  anoDoDizimo ='%s' group by mesDoDizimo order by field(mesDoDizimo, 'Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')" %ano);
	return dictfetchall(query)

def totalOfertaAno(ano):
	query = connection.cursor()
	query.execute("select sum(valorDaOferta) as totalOferta,anoDaOferta, mesDaOferta, dataDaOferta from DjangoOnIis_oferta where  anoDaOferta ='%s' group by mesDaOferta order by field(mesDaOferta, 'Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')" %ano);
	return dictfetchall(query)

def totalContribuicaoAno(ano):
	query = connection.cursor()
	query.execute("select sum(valorDaContribuicao) as totalContribuicao,anoDaContribuicao, mesDaContribuicao, dataDaContribuicao, descricaoDoProjeto from DjangoOnIis_contribuicao, DjangoOnIis_projeto where DjangoOnIis_projeto.id=DjangoOnIis_contribuicao.descricaoDaContribuicao_id and  anoDaContribuicao ='%s' group by descricaoDaContribuicao_id order by anoDaContribuicao" %ano);
	return dictfetchall(query)




def pesquisarMembro(request):

	content =''
	opcao = request.GET.get('opcao')
	informacao = request.GET.get('informacao')
	print informacao
	print opcao
	if opcao == 'Nome':
		resultado = get_nome(informacao)
		content ={'query':opcao, 'resultado':resultado}
	elif opcao == 'Numero de Membro':
		resultado = get_numero_membro(informacao)
		content = {'query':opcao, 'resultado':resultado}
	elif opcao == 'Profissao':
		resultado = get_profissao_membro(informacao)
		content = {'query':opcao, 'resultado':resultado}
	elif opcao == 'Funcao':
		resultado = get_funcao_membro(informacao)
		content = {'query':opcao, 'resultado':resultado}
	elif opcao == 'Todos':
		resultado = get_todos(informacao)
		content = {'query':opcao, 'resultado':resultado}
	else:
		resultado = get_grau_membro(informacao)
		content = {'query':opcao, 'resultado':resultado}

	template = 'pesquisarMembro.html'

	return render(request, template, content)



def lista_pacientes(request):
	paciente = get_lista_pacientes()
	template = 'lista_pacientes.html'
	return render(request, template, {'paciente':paciente})


def editarMembro(request):
	valor = request.GET.get('id')
	
	resultado = get_editar_membro(valor)
	print resultado
	if request.method == 'POST':
		form = MembroForm(request.POST, request.FILES)
		if form.is_valid():
			resultado = Membro.objects.get(pk=valor)
			resultado.provincia = Provincia.objects.get(nomeDaProvincia=form.cleaned_data['provincia'])
			resultado.pais = Pais.objects.get(nomeDoPais=form.cleaned_data['pais'])
			resultado.departamento = Departamento.objects.get(nomeDoDepartamento=form.cleaned_data['departamento'])
			resultado.igreja = Igreja.objects.get(nomeDaIgreja=form.cleaned_data['igreja'])
			resultado.nomeDoMembro = form.cleaned_data['nomeDoMembro']
			resultado.estadoCivil = form.cleaned_data['estadoCivil']
			resultado.sexo = form.cleaned_data['sexo']
			resultado.cargo = form.cleaned_data['cargo']
			resultado.funcaoNaIgreja = form.cleaned_data['funcaoNaIgreja']
			resultado.endereco = form.cleaned_data['endereco']
			resultado.bairro = form.cleaned_data['bairro']
			resultado.caixaPostal = form.cleaned_data['caixaPostal']
			resultado.telefone = form.cleaned_data['telefone']
			resultado.email = form.cleaned_data['email']
			resultado.dataDeNascimento = form.cleaned_data['dataDeNascimento']
			resultado.grauAcademico = form.cleaned_data['grauAcademico']
			resultado.profissao = form.cleaned_data['profissao']
			resultado.numeroDeIdentificacao = form.cleaned_data['numeroDeIdentificacao']
			resultado.conjuge = form.cleaned_data['conjuge']
			resultado.filiacaoPai = form.cleaned_data['filiacaoPai']
			resultado.filiacaoMae = form.cleaned_data['filiacaoMae']
			resultado.dataDeConversao = form.cleaned_data['dataDeConversao']
			resultado.procedencia = form.cleaned_data['procedencia']
			resultado.formaDeAdmissao = form.cleaned_data['formaDeAdmissao']
			resultado.dataDeBaptismo = form.cleaned_data['dataDeBaptismo']
			resultado.localDeBaptismo = form.cleaned_data['localDeBaptismo']
			resultado.dataDeConsagracaoDiacono = form.cleaned_data['dataDeConsagracaoDiacono']
			resultado.dataDeConsagracaoEvangelista = form.cleaned_data['dataDeConsagracaoEvangelista']
			resultado.dataDeConsagracaoPastor = form.cleaned_data['dataDeConsagracaoPastor']
			resultado.dataDeConsagracaoMissionario = form.cleaned_data['dataDeConsagracaoMissionario']
			resultado.numeroDeMembro = form.cleaned_data['numeroDeMembro']
			resultado.foto=request.FILES['foto']
			resultado.save()
			return HttpResponseRedirect('/gestao/membro/pesquisar/')

	else:
		form = MembroForm()
	template = 'editarMembro.html' 
	provincia=Provincia.objects.all()
	pais =Pais.objects.all()
	departamento=Departamento.objects.all()
	igreja=Igreja.objects.all()
	return render (request,template,{'form':form, 'resultado':resultado,'provincia':provincia,'pais':pais,'departamento':departamento,'igreja':igreja})




def eliminarMembro(request):
	valor = request.GET.get('id')
	print valor
	resultado = get_editar_membro(valor)
	print resultado
	
	if request.method == 'POST':
		form = MembroForm(request.POST)
		removerMembro(valor)
		return HttpResponseRedirect('/gestao/membro/pesquisar/')
	else:
		form = MembroForm()
	template = 'eliminarMembro.html'
	return render(request, template, {'form':form, 'resultado':resultado})


def visualizarMembro(request):
	valor = request.GET.get('id')
	print valor
	resultado = get_editar_membro(valor)
	print resultado
	
	if request.method == 'POST':
		form = MembroForm(request.POST)
		return HttpResponseRedirect('/gestao/membro/pesquisar/')
	else:
		form = MembroForm()
	template = 'visualizarMembro.html'
	provincia=Provincia.objects.all()
	pais =Pais.objects.all()
	departamento=Departamento.objects.all()
	igreja=Igreja.objects.all()
	return render (request,template,{'form':form, 'resultado':resultado,'provincia':provincia,'pais':pais,'departamento':departamento,'igreja':igreja})


def dizimo(request):
	if request.method =='POST':
		form = DizimoForm(request.POST)
		if form.is_valid():

			nomeDoMembro = Membro.objects.get(nomeDoMembro=form.cleaned_data['nomeDoMembro'])
			igreja = Igreja.objects.get(nomeDaIgreja=form.cleaned_data['igreja'])
			valorDoDizimo = form.cleaned_data['valorDoDizimo']
			dataDoDizimo = form.cleaned_data['dataDoDizimo']
			mesDoDizimo = form.cleaned_data['mesDoDizimo']
			anoDoDizimo = form.cleaned_data['anoDoDizimo']
			#print form.cleaned_data['nome']

			new_dizimo, created = Dizimo.objects.get_or_create(nomeDoMembro=nomeDoMembro, igreja=igreja, valorDoDizimo=valorDoDizimo,dataDoDizimo=dataDoDizimo,
				mesDoDizimo=mesDoDizimo, anoDoDizimo=anoDoDizimo)

	else:
		form = DizimoForm()
	valor = request.GET.get('id')
	request.session['id']=valor
	if not request.session['id']:
		membro = Membro.objects.order_by('nomeDoMembro')
	else:
		membro = Membro.objects.filter(pk=request.session['id'])

	template = 'dizimo.html'
	igreja = Igreja.objects.order_by('nomeDaIgreja')
	print membro

	return render(request, template, {'form':form, 'membro':membro, 'igreja':igreja})

def get_editar_dizimo(valor):
	query = connection.cursor()
	query.execute("select * from DjangoOnIis_dizimo where id='%s'" %valor)
	return dictfetchall(query)

def editarDizimo(request):
	valor = request.GET.get('id')
	request.session['id'] = valor
	resultado = get_editar_dizimo(request.session['id'])
	if request.method == 'POST':
		form = DizimoForm(request.POST)
		if form.is_valid():
			nomeDoMembro = Membro.objects.get(nomeDoMembro=form.cleaned_data['nomeDoMembro'])
			igreja = Igreja.objects.get(nomeDaIgreja=form.cleaned_data['igreja'])
			valorDoDizimo = form.cleaned_data['valorDoDizimo']
			dataDoDizimo = form.cleaned_data['dataDoDizimo']
			mesDoDizimo = form.cleaned_data['mesDoDizimo']
			anoDoDizimo = form.cleaned_data['anoDoDizimo']
			

			created = Dizimo.objects.filter(pk=request.session['id']).update(nomeDoMembro=nomeDoMembro, igreja=igreja, valorDoDizimo=valorDoDizimo,dataDoDizimo=dataDoDizimo,
				mesDoDizimo=mesDoDizimo, anoDoDizimo=anoDoDizimo)
			return HttpResponseRedirect('/gestao/membro/pesquisar/')

	else:
		form = DizimoForm()
	membro = Membro.objects.filter(pk=resultado[0]['nomeDoMembro_id'])
	igreja = Igreja.objects.filter(pk=resultado[0]['igreja_id'])
	template = 'editarDizimo.html'
	return render(request, template, {'form':form, 'resultado':resultado, 'igreja':igreja, 'membro':membro})


def eliminarDizimo(request):
	valor = request.GET.get('id')
	request.session['id']=valor 
	resultado = get_editar_dizimo(request.session['id'])
	try:
		if request.method == 'POST':
			resultado = Dizimo.objects.filter(pk=request.session['id']).delete()
			return HttpResponseRedirect('/gestao/financas/contribuicao/pesquisar/')

		template = 'eliminarDizimo.html'
		membro = Membro.objects.filter(pk=resultado[0]['nomeDoMembro_id'])
		igreja = Igreja.objects.filter(pk=resultado[0]['igreja_id'])
	except IndexError:
		return HttpResponseRedirect('/gestao/membro/pesquisar/')

	return render(request, template, {'resultado':resultado, 'membro':membro})


def projeto(request):
	if request.method=='POST':
		form = ProjetoForm(request.POST)
		if form.is_valid():
			igreja = Igreja.objects.get(nomeDaIgreja=form.cleaned_data['igreja'])
			descricaoDoProjeto = form.cleaned_data['descricaoDoProjeto']
			orcamento = form.cleaned_data['orcamento']

			new_projeto, created = Projeto.objects.get_or_create(igreja=igreja, descricaoDoProjeto=descricaoDoProjeto, orcamento=orcamento)
			return HttpResponseRedirect('/gestao/financas/projetos/pesquisar/')

	else:
		form = ProjetoForm()

	template = 'projeto.html'
	igreja = Igreja.objects.order_by('nomeDaIgreja')
	return render(request, template, {'form':form, 'igreja':igreja})

def contribuicao(request):
	if request.method=='POST':
		form = ContribuicaoForm(request.POST)
		if form.is_valid():
			nomeDoMembro = Membro.objects.get(nomeDoMembro=form.cleaned_data['nomeDoMembro'])
			igreja = Igreja.objects.get(nomeDaIgreja=form.cleaned_data['igreja'])
			valorDaContribuicao = form.cleaned_data['valorDaContribuicao']
			descricaoDaContribuicao = Projeto.objects.get(descricaoDoProjeto=form.cleaned_data['descricaoDaContribuicao'])
			dataDaContribuicao = form.cleaned_data['dataDaContribuicao']
			mesDaContribuicao = form.cleaned_data['mesDaContribuicao']
			anoDaContribuicao = form.cleaned_data['anoDaContribuicao']
			new_contribuicao, created = Contribuicao.objects.get_or_create(nomeDoMembro=nomeDoMembro,igreja=igreja,valorDaContribuicao=valorDaContribuicao,descricaoDaContribuicao=descricaoDaContribuicao, dataDaContribuicao=dataDaContribuicao,
				mesDaContribuicao=mesDaContribuicao, anoDaContribuicao=anoDaContribuicao)

			return HttpResponseRedirect('/gestao/financas/contribuicao/pesquisar/')
	else:
		form = ContribuicaoForm()

	template = 'contribuicao.html'
	valor = request.GET.get('id')
	request.session['id'] = valor
	if not request.session['id']:
		membro = Membro.objects.order_by('nomeDoMembro')
	else:
		membro = Membro.objects.filter(pk=request.session['id'])
	igreja = Igreja.objects.order_by('nomeDaIgreja')
	projeto= Projeto.objects.order_by('descricaoDoProjeto')
	return render (request, template, {'form':form, 'membro':membro, 'igreja':igreja ,'projeto':projeto})

def get_editar_contribuicao(valor):
	query = connection.cursor()
	query.execute("select * from DjangoOnIis_contribuicao where id='%s'" %valor)
	return dictfetchall(query)

def editarContribuicao(request):
	valor = request.GET.get('id')
	request.session['id'] = valor
	resultado = get_editar_contribuicao(request.session['id'])
	if request.method == 'POST':
		form = ContribuicaoForm(request.POST)
		if form.is_valid():
			nomeDoMembro = Membro.objects.get(nomeDoMembro=form.cleaned_data['nomeDoMembro'])
			igreja = Igreja.objects.get(nomeDaIgreja=form.cleaned_data['igreja'])
			valorDaContribuicao = form.cleaned_data['valorDaContribuicao']
			descricaoDaContribuicao = Projeto.objects.get(descricaoDoProjeto=form.cleaned_data['descricaoDaContribuicao'])
			dataDaContribuicao = form.cleaned_data['dataDaContribuicao']
			mesDaContribuicao = form.cleaned_data['mesDaContribuicao']
			anoDaContribuicao = form.cleaned_data['anoDaContribuicao']
			created = Contribuicao.objects.filter(pk=request.session['id']).update(nomeDoMembro=nomeDoMembro,igreja=igreja,valorDaContribuicao=valorDaContribuicao,descricaoDaContribuicao=descricaoDaContribuicao, dataDaContribuicao=dataDaContribuicao,
				mesDaContribuicao=mesDaContribuicao, anoDaContribuicao=anoDaContribuicao)

			return HttpResponseRedirect('/gestao/financas/contribuicao/pesquisar/')
	else:
		form = ContribuicaoForm()
	membro = Membro.objects.filter(pk=resultado[0]['nomeDoMembro_id'])
	igreja = Igreja.objects.filter(pk=resultado[0]['igreja_id'])
	projeto = Projeto.objects.order_by('descricaoDoProjeto')
	template = 'editarContribuicao.html'

	return render(request, template, {'form':form, 'resultado':resultado, 'membro':membro, 'igreja':igreja, 'projeto':projeto})

def eliminarContribuicao(request):
	valor = request.GET.get('id')
	request.session['id']=valor 
	resultado = get_editar_contribuicao(request.session['id'])
	try:
		if request.method == 'POST':
			resultado = Contribuicao.objects.filter(pk=request.session['id']).delete()
			return HttpResponseRedirect('/gestao/financas/contribuicao/pesquisar/')

		template = 'eliminarContribuicao.html'
		membro = Membro.objects.filter(pk=resultado[0]['nomeDoMembro_id'])
		igreja = Igreja.objects.filter(pk=resultado[0]['igreja_id'])
		projeto = Projeto.objects.filter(pk=resultado[0]['descricaoDaContribuicao_id'])
	except IndexError:
		return HttpResponseRedirect('/gestao/financas/contribuicao/pesquisar/')

	return render(request, template, {'resultado':resultado, 'membro':membro, 'projeto':projeto})

def oferta(request):
	if request.method=='POST':
		form = OfertaForm(request.POST)
		if form.is_valid():
			igreja = Igreja.objects.get(nomeDaIgreja=form.cleaned_data['igreja'])
			valorDaOferta = form.cleaned_data['valorDaOferta']
			dataDaOferta =form.cleaned_data['dataDaOferta']
			mesDaOferta = form.cleaned_data['mesDaOferta']
			anoDaOferta = form.cleaned_data['anoDaOferta']

			new_oferta, created = Oferta.objects.get_or_create(igreja=igreja,valorDaOferta=valorDaOferta, dataDaOferta=dataDaOferta,
				mesDaOferta=mesDaOferta, anoDaOferta=anoDaOferta)
			return HttpResponseRedirect('/gestao/financas/ofertas/pesquisar/')
	else:
		form = ContribuicaoForm()

	template = 'oferta.html'
	igreja = Igreja.objects.order_by('nomeDaIgreja')
	return render (request, template, {'form':form, 'igreja':igreja})


def visualizarDizimo(request):
	valor = request.GET.get('id')
	ano = request.GET.get('ano')
	if request.GET.get('id'):
		request.session['id'] = valor

	resultado = pesquisarDizimoTodos(valor)
	if ano and ano!='Todos':
		resultado=Dizimo.objects.filter(nomeDoMembro_id=request.session['id'], anoDoDizimo=ano)

	else:
		resultado = Dizimo.objects.filter(nomeDoMembro_id=request.session['id'])

	membro = Membro.objects.filter(pk=request.session['id'])
		
	template = 'visualizarDizimo.html'
	return render(request, template, {'resultado':resultado, 'membro':membro})

def totalValores(request):
	opcao = request.GET.get('anoescolha')
	print opcao
	resultado = ''
	if opcao:
		resultado = totalAno(opcao)
		print resultado
	template = 'totalValoresDizimos.html'
	return render(request, template, {'resultado':resultado})



def funcionario(request):
	if request.method == 'POST':
		form = FuncionarioForm(request.POST,request.FILES)
		if form.is_valid():
			nomeDoFuncionario = form.cleaned_data['nomeDoFuncionario']
			estadoCivil = form.cleaned_data['estadoCivil']
			sexo = form.cleaned_data['sexo']
			cargo = form.cleaned_data['cargo']
			endereco = form.cleaned_data['endereco']
			bairro = form.cleaned_data['bairro']
			provincia = Provincia.objects.get(nomeDaProvincia=form.cleaned_data['provincia'])
			caixaPostal = form.cleaned_data['caixaPostal']
			telefone = form.cleaned_data['telefone']
			email = form.cleaned_data['email']
			dataDeNascimento = form.cleaned_data['dataDeNascimento']
			pais = Pais.objects.get(nomeDoPais=form.cleaned_data['pais'])
			grauAcademico = form.cleaned_data['grauAcademico']
			profissao = form.cleaned_data['profissao']
			numeroDeIdentificacao = form.cleaned_data['numeroDeIdentificacao']
			filiacaoPai = form.cleaned_data['filiacaoPai']
			filiacaoMae = form.cleaned_data['filiacaoMae']
			numeroDeFuncionario = form.cleaned_data['numeroDeFuncionario']
			salarioBase = form.cleaned_data['salarioBase']
			

			new_funcionario= Funcionario(nomeDoFuncionario=nomeDoFuncionario,estadoCivil=estadoCivil,
				sexo=sexo, cargo=cargo, endereco=endereco, bairro=bairro, provincia=provincia,caixaPostal=caixaPostal, telefone=telefone,
				email=email, dataDeNascimento=dataDeNascimento, pais=pais, grauAcademico=grauAcademico, profissao=profissao,
				numeroDeIdentificacao=numeroDeIdentificacao, filiacaoPai=filiacaoPai, filiacaoMae=filiacaoMae, numeroDeFuncionario=numeroDeFuncionario,
				salarioBase=salarioBase,foto=request.FILES['foto'])
			new_funcionario.save()
			return HttpResponseRedirect('/gestao/rh/funcionario/pesquisar/')
	else:
		form= FuncionarioForm()
	pais = Pais.objects.order_by('nomeDoPais')
	provincia = Provincia.objects.order_by('nomeDaProvincia')
	template = 'funcionario.html'
	return render(request, template, {'form':form, 'pais':pais, 'provincia':provincia})

def get_funcionario(informacao):
	query = connection.cursor()
	query.execute("select * from DjangoOnIis_funcionario where nomeDoFuncionario='%s'" %informacao)
	return dictfetchall(query)

def get_funcionarioId(informacao):
	query = connection.cursor()
	query.execute("select * from DjangoOnIis_funcionario where numeroDeFuncionario='%s'" %informacao)
	return dictfetchall(query)

def pesquisarFuncionario(request):
	opcao = request.GET.get('opcao')
	informacao = request.GET.get('informacao')

	if opcao == 'Todos':
		resultado = Funcionario.objects.order_by('nomeDoFuncionario')
	elif opcao == 'Nome':
		resultado = get_funcionario(informacao)
	else:
		resultado = get_funcionarioId(informacao)

	pais = Pais.objects.order_by('pais')
	provincia = Provincia.objects.order_by('provincia')
	template = 'pesquisarFuncionario.html'
	return render(request, template, {'resultado':resultado, 'pais':pais, 'provincia':provincia})



def get_salario(funcionario, ano):
	query = connection.cursor()
	query.execute("select * from DjangoOnIis_salario where nomeDoFuncionario_id='%s' and salarioAno='%s'" %(funcionario, ano))
	return dictfetchall(query)

def get_salarioTodos(funcionario):
	query = connection.cursor()
	query.execute("select * from DjangoOnIis_salario where nomeDoFuncionario_id='%s'" %funcionario)
	return dictfetchall(query)

def get_editar_salario(valor):
	query = connection.cursor()
	query.execute("select * from DjangoOnIis_salario where id='%s'" %valor)
	return dictfetchall(query)


def visualizarSalario(request):
	valor = request.GET.get('id')
	ano = request.GET.get('ano')
	print ano

	if request.GET.get('id'):
		request.session['id'] = valor
	resultado=get_salarioTodos(valor)
	if ano and ano!='Todos':
		resultado = get_salario(request.session['id'],ano)
	else:
		resultado = get_salarioTodos(request.session['id'])
	
	funcionario = Funcionario.objects.get(pk=request.session['id'])
	print funcionario.salarioBase
	template= 'visualizarSalario.html'
	return render(request, template, {'resultado':resultado, 'funcionario':funcionario})


def inserirSalario(request):

	if request.method=='POST':
		form = SalarioForm(request.POST)
		if form.is_valid():
			nomeDoFuncionario=Funcionario.objects.get(nomeDoFuncionario=form.cleaned_data['nomeDoFuncionario'])
			salarioAno = form.cleaned_data['salarioAno']
			salarioMes= form.cleaned_data['salarioMes']
			salarioSS = form.cleaned_data['salarioSS']
			salarioIRT = form.cleaned_data['salarioIRT']
			salarioNumerodeFaltas = form.cleaned_data['salarioNumerodeFaltas']
			salarioBonus = form.cleaned_data['salarioBonus']
			salarioLiquido = form.cleaned_data['salarioLiquido']

			new_salario, created = Salario.objects.get_or_create(nomeDoFuncionario=nomeDoFuncionario, salarioAno=salarioAno,
					salarioMes=salarioMes, salarioSS=salarioSS, salarioIRT=salarioIRT, salarioNumerodeFaltas=salarioNumerodeFaltas,
					salarioBonus=salarioBonus, salarioLiquido=salarioLiquido)
			return HttpResponseRedirect('/gestao/rh/funcionario/pesquisar/')

	else:
		form=SalarioForm()
	valor = request.GET.get('id')
	request.session['id'] =valor
	if not request.session['id']:
		funcionario = Funcionario.objects.order_by('nomeDoFuncionario') 
	else:
		funcionario = Funcionario.objects.filter(pk=request.session['id'])
	template = 'inserirSalario.html'
	return render(request, template, {'form':form, 'funcionario':funcionario})

def EditarSalario(request):
	valor = request.GET.get('id')
	resultado = get_editar_salario(valor)
	print resultado
	if request.method == 'POST':
		form = SalarioForm(request.POST)
		if form.is_valid():
			nomeDoFuncionario=Funcionario.objects.get(nomeDoFuncionario=form.cleaned_data['nomeDoFuncionario'])
			salarioAno = form.cleaned_data['salarioAno']
			salarioMes= form.cleaned_data['salarioMes']
			salarioSS = form.cleaned_data['salarioSS']
			salarioIRT = form.cleaned_data['salarioIRT']
			salarioNumerodeFaltas = form.cleaned_data['salarioNumerodeFaltas']
			salarioBonus = form.cleaned_data['salarioBonus']
			salarioLiquido = form.cleaned_data['salarioLiquido']

			created = Salario.objects.filter(pk=valor).update(nomeDoFuncionario=nomeDoFuncionario, salarioAno=salarioAno,
					salarioMes=salarioMes, salarioSS=salarioSS, salarioIRT=salarioIRT, salarioNumerodeFaltas=salarioNumerodeFaltas,
					salarioBonus=salarioBonus, salarioLiquido=salarioLiquido)
			return HttpResponseRedirect('/gestao/rh/funcionario/pesquisar/')
	else:
		form=SalarioForm()

	funcionario = Funcionario.objects.get(pk=resultado[0]['nomeDoFuncionario_id']) 
	template = 'editarSalario.html'
	return render(request, template, {'form':form, 'funcionario':funcionario, 'resultado':resultado})


def removeSalario(valor):
	query = connection.cursor()
	query.execute("delete from DjangoOnIis_salario where id='%s'" %valor)
	return dictfetchall(query)

def eliminarSalario(request):
	valor = request.GET.get('id')
	resultado = get_editar_salario(valor)
	if request.method == 'POST':
		form= SalarioForm(request.POST)
		removeSalario(valor)
		return HttpResponseRedirect('/gestao/rh/funcionario/pesquisar/')
	else:
		form=SalarioForm()

	template = 'eliminarSalarioMes.html'
	funcionario = Funcionario.objects.get(pk=resultado[0]['nomeDoFuncionario_id']) 
	return render(request, template, {'form':form, 'funcionario':funcionario, 'resultado':resultado})


def visualizarFuncionario(request):
	valor = request.GET.get('id')
	resultado = Funcionario.objects.get(pk=valor)
	pais = Pais.objects.get(pk=resultado.pais_id)
	provincia = Provincia.objects.get(pk=resultado.provincia_id)
	template = 'visualizarFuncionario.html'

	return render (request,template,{'resultado':resultado, 'pais':pais, 'provincia':provincia})


def editarFuncionario(request):
	valor = request.GET.get('id')
	resultado = Funcionario.objects.get(pk=valor)
	print resultado
	if request.method == 'POST':
		form = FuncionarioForm(request.POST,request.FILES)
		if form.is_valid():
			resultado = Funcionario.objects.get(pk=valor)
			resultado.nomeDoFuncionario = form.cleaned_data['nomeDoFuncionario']
			resultado.estadoCivil = form.cleaned_data['estadoCivil']
			resultado.sexo = form.cleaned_data['sexo']
			resultado.cargo = form.cleaned_data['cargo']
			resultado.endereco = form.cleaned_data['endereco']
			resultado.bairro = form.cleaned_data['bairro']
			resultado.provincia = Provincia.objects.get(nomeDaProvincia=form.cleaned_data['provincia'])
			resultado.caixaPostal = form.cleaned_data['caixaPostal']
			resultado.telefone = form.cleaned_data['telefone']
			resultado.email = form.cleaned_data['email']
			resultado.dataDeNascimento = form.cleaned_data['dataDeNascimento']
			resultado.pais = Pais.objects.get(nomeDoPais=form.cleaned_data['pais'])
			resultado.grauAcademico = form.cleaned_data['grauAcademico']
			resultado.profissao = form.cleaned_data['profissao']
			resultado.numeroDeIdentificacao = form.cleaned_data['numeroDeIdentificacao']
			resultado.filiacaoPai = form.cleaned_data['filiacaoPai']
			resultado.filiacaoMae = form.cleaned_data['filiacaoMae']
			resultado.numeroDeFuncionario = form.cleaned_data['numeroDeFuncionario']
			resultado.salarioBase = form.cleaned_data['salarioBase']
			resultado.foto=request.FILES['foto']
			resultado.save()
			return HttpResponseRedirect('/gestao/rh/funcionario/pesquisar/')
	else:
		form= FuncionarioForm()
	pais = Pais.objects.order_by('nomeDoPais')
	provincia = Provincia.objects.order_by('nomeDaProvincia')
	template = 'editarFuncionario.html'
	return render(request, template, {'form':form, 'pais':pais, 'provincia':provincia, 'resultado':resultado})

def eliminarFuncionario(request):
	valor = request.GET.get('id')
	resultado = Funcionario.objects.get(pk=valor)
	if request.method == 'POST':
		resultado = Funcionario.objects.filter(pk=valor).delete()
		return HttpResponseRedirect('/gestao/rh/funcionario/pesquisar/')
	
	template = 'eliminarFuncionario.html'
	return render(request, template, {'resultado':resultado})


def equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            igreja = Igreja.objects.get(nomeDaIgreja=form.cleaned_data['igreja'])
            nome=form.cleaned_data['nome']
            marca = form.cleaned_data['marca']
            numeroDeSerie = form.cleaned_data['numeroDeSerie']
            dataDaAquisicao = form.cleaned_data['dataDaAquisicao']
            modelo = form.cleaned_data['modelo']
            localizacao = form.cleaned_data['localizacao']
            estado = form.cleaned_data['estado']
            preco = form.cleaned_data['preco']
            obs = form.cleaned_data['obs']

            new_equipamento, created=Equipamento.objects.get_or_create(igreja=igreja,nome=nome,marca=marca,numeroDeSerie=numeroDeSerie,dataDaAquisicao=dataDaAquisicao,modelo=modelo,localizacao=localizacao,estado=estado,preco=preco,obs=obs)
            
    else:
        form = EquipamentoForm()
    template='equipamento.html'
    igreja = Igreja.objects.order_by('nomeDaIgreja')
    return render (request, template, {'form':form, 'igreja':igreja})


def pesquisarEquipamentos(estado):
    query = connection.cursor()
    query.execute("select * from DjangoOnIis_equipamento where estado = '%s'" %estado);
    return dictfetchall(query)

def pesquisarEquipamentoTodos():
    query = connection.cursor()
    query.execute("select * from DjangoOnIis_equipamento ");
    return dictfetchall(query)

def pesquisarEquipamento(request):
    opcao = request.GET.get('estado')
    print opcao
    resultado = ''
    if opcao is not None and opcao != '':
        resultado = pesquisarEquipamentos(opcao)
    else:
        resultado=pesquisarEquipamentoTodos()
    igreja = Igreja.objects.order_by('nomeDaIgreja')
    template = 'pesquisarEquipamento.html'
    return render(request, template, {'resultado':resultado,'igreja':igreja})

def removerEquipamento(valor):
    query = connection.cursor()
    query.execute("delete from DjangoOnIis_equipamento where id = '%s'" % valor);
    return dictfetchall(query)

def get_editar_equipamento(valor):
    query = connection.cursor()
    query.execute("select * from DjangoOnIis_equipamento where id = '%s'" % valor);
    return dictfetchall(query)

def editarEquipamento(request):
    valor = request.GET.get('id')


    
    resultado = get_editar_equipamento(valor)

    print resultado
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            igreja = Igreja.objects.get(nomeDaIgreja=form.cleaned_data['igreja'])
            nome=form.cleaned_data['nome']
            marca = form.cleaned_data['marca']
            numeroDeSerie = form.cleaned_data['numeroDeSerie']
            dataDaAquisicao = form.cleaned_data['dataDaAquisicao']
            modelo = form.cleaned_data['modelo']
            localizacao = form.cleaned_data['localizacao']
            estado = form.cleaned_data['estado']
            preco = form.cleaned_data['preco']
            obs = form.cleaned_data['obs']

            created=Equipamento.objects.filter(pk=valor).update(igreja=igreja,nome=nome,marca=marca,numeroDeSerie=numeroDeSerie,dataDaAquisicao=dataDaAquisicao,modelo=modelo,localizacao=localizacao,estado=estado,preco=preco,obs=obs)
            return HttpResponseRedirect('/gestao/inventario/pesquisar/')
    else:
        form = EquipamentoForm()
    template='editarEquipamento.html'
    igreja = Igreja.objects.order_by('nomeDaIgreja')
    return render (request, template, {'form':form, 'igreja':igreja,'resultado':resultado})



def eliminarEquipamento(request):
    valor = request.GET.get('id')
    print valor
    resultado = get_editar_equipamento(valor)
    print resultado
    
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        removerEquipamento(valor)
        return HttpResponseRedirect('/gestao/inventario/pesquisar/')
    else:
        form = MembroForm()
    template = 'eliminarEquipamento.html'
    return render(request, template, {'form':form, 'resultado':resultado})


def pesquisarProjecto(request):
	nome = request.GET.get('descricaoDoProjeto')
	print 'nome:', nome
	resultado = ''

	if nome=='Todos':
		resultado = Projeto.objects.order_by('descricaoDoProjeto')
	else:
		resultado = Projeto.objects.filter(descricaoDoProjeto=nome)
	template = 'pesquisarProjecto.html'
	descricaoDoProjeto = Projeto.objects.order_by('descricaoDoProjeto')

	return render(request, template, {'resultado':resultado, 'descricaoDoProjeto':descricaoDoProjeto})

def editarProjecto(request):

	valor = request.GET.get('id')
	resultado = Projeto.objects.get(pk=valor)
	if request.method == 'POST':
		form = ProjetoForm(request.POST)
		if form.is_valid():
			igreja = Igreja.objects.get(nomeDaIgreja=form.cleaned_data['igreja'])
			descricaoDoProjeto = form.cleaned_data['descricaoDoProjeto']
			orcamento = form.cleaned_data['orcamento']

			created = Projeto.objects.filter(pk=valor).update(igreja=igreja, descricaoDoProjeto=descricaoDoProjeto, orcamento=orcamento)
			return HttpResponseRedirect('/gestao/financas/projetos/pesquisar/')
	else:
		form = ProjetoForm()
	template = 'editarProjecto.html'
	igreja = Igreja.objects.order_by('nomeDaIgreja')
	return render(request, template,{'form':form, 'resultado':resultado, 'igreja':igreja})

def eliminarProjecto(request):
	valor = request.GET.get('id')
	resultado = Projeto.objects.get(pk=valor)
	if request.method == 'POST':
		resultado = Projeto.objects.filter(pk=valor).delete()
		return HttpResponseRedirect('/gestao/financas/projetos/pesquisar/')

	template = 'eliminarProjecto.html'
	return render(request, template, {'resultado':resultado})


def pesquisarOferta(request):
	opcao = request.GET.get('anoescolha')
	resultado = ''
	if opcao:
		resultado = totalOfertaAno(opcao)

	template = 'pesquisarOferta.html'
	return render(request, template, {'resultado':resultado})

def visualizarContribuicao(request):
	valor = request.GET.get('id')
	ano = request.GET.get('ano')
	if request.GET.get('id'):
		request.session['id'] = valor

	resultado = pesquisarContribuicaoTodos(valor)
	if ano and ano!='Todos':
		resultado=pesquisarContribuicao(request.session['id'],ano)
	else:
		resultado = pesquisarContribuicaoTodos(request.session['id'])

	membro = Membro.objects.filter(pk=request.session['id'])	
	template = 'visualizarContribuicao.html'
	return render(request, template, {'resultado':resultado, 'membro':membro})


def pesquisarContribuicao(request):
	opcao = request.GET.get('anoescolha')
	resultado = ''
	if opcao:
		resultado = totalContribuicaoAno(opcao)
		print 'Resultado',resultado

	template = 'pesquisarContribuicao.html'
	return render(request, template, {'resultado':resultado})


from .models import Noticias

def get_noticias():
	query = connection.cursor()
	query.execute("select id,left(noticia,100) as noticia, titulo,foto,dataPublicacao,tipo from DjangoOnIis_noticias order by dataPublicacao desc");
	return dictfetchall(query)


def get_noticias_unica(idd):
	query = connection.cursor()
	query.execute("select id,noticia, titulo,foto,dataPublicacao,tipo from DjangoOnIis_noticias where id = '%s'" % idd);
	return dictfetchall(query)

def get_comentarios(idd):
	query = connection.cursor()
	query.execute("select * from DjangoOnIis_comentarios where noticia_id = '%s' order by id desc" % idd);
	return dictfetchall(query)

def noticias(request):
	resultado=get_noticias()
	form = NoticiasForm()
	resultado2 = Noticias.objects.all()

	
	#membro = resultado[0]['funcionario_id']
	#funcionario = get_editar_membro(membro)
	#print 'resultado fot ', resultado[0]['foto']

	#print 'funcionario'
	#print funcionario
	template = 'noticias.html'
	return render(request,template,{'form':form,'resultado':resultado})


def publicarNoticia(request):
	if request.method== 'POST':
		form=NoticiasForm(request.POST, request.FILES)
		if form.is_valid():
			print 'olaaaaa'
		
			
			
			
			
			new_foto = Noticias(foto=request.FILES['foto'],titulo = form.cleaned_data['titulo'],noticia=form.cleaned_data['noticia'],
				funcionario=Membro.objects.get(nomeDoMembro=form.cleaned_data['funcionario']),dataPublicacao = form.cleaned_data['dataPublicacao'],tipo=form.cleaned_data['tipo'])
			foto = new_foto.save()
			return HttpResponseRedirect('/gestao/')

			

		

			#new_publicarNoticia, created=Noticias.objects.get_or_create(titulo=titulo,noticia=noticia,foto=foto)
	else:
		form=NoticiasForm()
	template='inserirNoticia.html'
	membro= Membro.objects.order_by('nomeDoMembro')
	noticias=Noticias.objects.all()
	return render(request,template,{'form':form,'membro':membro,'noticia':noticias})








#CONFIGURAÇÕES

from .forms import ConfiguracoesForm
from .models import Configuracoes
from datetime import date

def configuracoes(request):

	if request.method=='POST':
		form = ConfiguracoesForm(request.POST,request.FILES)
		if form.is_valid():


			new_configuracoes=Configuracoes(igreja = Igreja.objects.get(nomeDaIgreja=form.cleaned_data['igreja']),imagem1=request.FILES['imagem1'],imagem2=request.FILES['imagem2'],texto1=form.cleaned_data['texto1'],
				texto2=form.cleaned_data['texto2'],texto3=form.cleaned_data['texto3'],texto4=form.cleaned_data['texto4'],texto5=form.cleaned_data['texto5']
				,texto6=form.cleaned_data['texto6'],desenvolvedores=form.cleaned_data['desenvolvedores'])
			imagem=new_configuracoes.save()
			return HttpResponseRedirect('/gestao/')

	else:
		form=ConfiguracoesForm()
	template='configuracoes.html'
	igreja = Igreja.objects.order_by('nomeDaIgreja')
	return render(request,template,{'form':form,'igreja':igreja})




#--------------------------------------------------Modulo Gestao de noticias---------------------------------------------------
def indexNoticias(request):
	resultado=get_noticias()
	form = NoticiasForm()
	resultado = get_noticias()
	configuracoes = Configuracoes.objects.all()
	template = 'indexNoticias.html'
	return render(request,template,{'form':form,'resultado':resultado,'configuracoes':configuracoes})



def lerNoticias(request):
	#print request.GET.get('id')
	if request.method=='POST':
		form = ComentariosForm(request.POST)
		if form.is_valid():
			print Membro.objects.get(nomeDoMembro=form.cleaned_data['autor'])
			print Noticias.objects.get(titulo=form.cleaned_data['noticia'])



			new_lerNoticias =Comentarios(autor = Membro.objects.get(nomeDoMembro=form.cleaned_data['autor']),noticia=Noticias.objects.get(titulo=form.cleaned_data['noticia'])
				,comentario=form.cleaned_data['comentario'],data=date.today())

			new_lerNoticias.save()
	else:
		form = ComentariosForm()

	idd = request.GET.get('id')
	resultado = get_noticias_unica(idd)
	comentarios = get_comentarios(idd)
	configuracoes = Configuracoes.objects.all()
	membro= Membro.objects.order_by('nomeDoMembro')
	template = 'lerNoticias.html'

	return render(request,template,{'form':form,'resultado':resultado,'configuracoes':configuracoes,'membro':membro,'comentarios':comentarios})




#HOME
def get_devocional():
	query = connection.cursor()
	query.execute("select id,left(noticia,100) as noticia, titulo,foto,dataPublicacao,tipo from DjangoOnIis_noticias where tipo='Evento' order by dataPublicacao desc");
	return dictfetchall(query)
def get_eventos():
	query = connection.cursor()
	query.execute("select id,left(noticia,100) as noticia, titulo,foto,dataPublicacao,tipo from DjangoOnIis_noticias where tipo='Evento' order by dataPublicacao desc");
	return dictfetchall(query)
def get_noticias_destaque():
	query = connection.cursor()
	query.execute("select id,noticia, titulo,foto,dataPublicacao,tipo from DjangoOnIis_noticias where tipo = 'Destaque' order by dataPublicacao desc limit 3");
	return dictfetchall(query)

def get_noticias_normal():
	query = connection.cursor()
	query.execute("select id,noticia, titulo,foto,dataPublicacao,tipo from DjangoOnIis_noticias where tipo = 'Normal' order by dataPublicacao desc limit 6");
	return dictfetchall(query)

def get_programa():
	query = connection.cursor()
	query.execute("select * from DjangoOnIis_programa order by field(diaDaSemana, 'Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira','Sexta-Feira','Sábado','Domingo')");
	return dictfetchall(query)


def home_site(request):
	template='home_site.html'
	noticias_destaques=get_noticias_destaque()
	noticia1 = ''
	noticia2 = ''
	noticia3 = ''
	try:
		for i in range(len(noticias_destaques)):
			if i==0:
				noticia1=noticias_destaques[i]
			elif i==1:
				noticia2=noticias_destaques[i]
			
			else:
				noticia3=noticias_destaques[i]
	except IndexError:
		noticia1=''
		noticia2=''
		noticia3=''

	devocional=Noticias.objects.filter(tipo='Devocional').order_by('-id')
	ultimo_devocional=Noticias.objects.filter(tipo='Devocional').last()
	programa= get_programa()

	eventos=get_eventos() #Noticias.objects.filter(tipo='Evento')
	noticiasNormais=get_noticias_normal()





	configuracoes = Configuracoes.objects.last()
	return render(request,template,{'configuracoes':configuracoes,'noticias_destaques':noticias_destaques, 'noticia1':noticia1,'noticia2':noticia2, 'noticia3':noticia3,'noticiasNormais':noticiasNormais,'eventos':eventos,'devocional':devocional,'ultimo_devocional':ultimo_devocional,'programa':programa})


def homeUm(request):
	template='homeUm.html'
	noticias_destaques=get_noticias_destaque()
	noticia1=noticias_destaques[0]
	noticia2=noticias_destaques[1]
	noticia3=noticias_destaques[2]
	devocional=Noticias.objects.filter(tipo='Devocional').order_by('-id')
	ultimo_devocional=Noticias.objects.filter(tipo='Devocional').last()

	eventos=get_eventos() #Noticias.objects.filter(tipo='Evento')
	noticiasNormais=get_noticias_normal()




	configuracoes = Configuracoes.objects.last()


	return render(request,template,{'configuracoes':configuracoes,'noticias_destaques':noticias_destaques, 'noticia1':noticia1,'noticia2':noticia2, 'noticia3':noticia3,'noticiasNormais':noticiasNormais,'eventos':eventos,'devocional':devocional,'ultimo_devocional':ultimo_devocional})

def pesquisarNoticia(request):
	
	tipo=request.GET.get('tipo')
	if tipo:
		resultado=Noticias.objects.filter(tipo=tipo).order_by('-dataPublicacao')
	if tipo==None or tipo=='Todos':
		resultado=Noticias.objects.all().order_by('-dataPublicacao')
	template='pesquisarNoticia.html'
	return render(request,template,{'resultado':resultado,'tipo':tipo})




def EditarNotica(request):
	idd = request.GET.get('id')
	resultado = Noticias.objects.get(pk=idd)
	print '-----------',resultado.noticia
	if request.method== 'POST':
		form=NoticiasForm(request.POST, request.FILES)
		if form.is_valid():
			print 'olaaaaa'			
			resultado = Noticias.objects.get(pk=idd)
			resultado.foto=request.FILES['foto']
			resultado.titulo = form.cleaned_data['titulo']
			resultado.noticia=form.cleaned_data['noticia']
			resultado.funcionario=Membro.objects.get(nomeDoMembro=form.cleaned_data['funcionario'])
			resultado.dataPublicacao = date.today()
			resultado.tipo=form.cleaned_data['tipo']
			resultado.save()
			return HttpResponseRedirect('/gestao/noticias/pesquisar/')

			#new_publicarNoticia, created=Noticias.objects.get_or_create(titulo=titulo,noticia=noticia,foto=foto)
	else:
		form=NoticiasForm()
	template='editarNoticia.html'
	membro= Membro.objects.order_by('nomeDoMembro')
	noticias=Noticias.objects.all()
	return render(request,template,{'form':form,'membro':membro,'noticia':noticias,'resultado':resultado})


def removerNoticia(valor):
	query = connection.cursor()
	query.execute("delete from DjangoOnIis_noticias where id = '%s'" % valor);
	return dictfetchall(query)


def eliminarNotica(request):
	idd = request.GET.get('id')
	print idd
	resultado = Noticias.objects.get(pk=idd)
	print resultado
	
	if request.method == 'POST':
		form = NoticiasForm(request.POST)
		removerNoticia(idd)
		return HttpResponseRedirect('/gestao/noticias/pesquisar/')
	else:
		form = NoticiasForm()
	template = 'eliminarNoticia.html'
	return render(request, template, {'form':form, 'resultado':resultado})




def cartaDeRecomendacao(request):

    # Create the HttpResponse object with the appropriate PDF headers.
    other = Membro.objects.last()
    nome = other.nomeDoMembro
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="carta de recomendacao.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = letter
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.setLineWidth(.3)
    p.drawCentredString(300,800,"Carta de Recomendação")
    #p.line(480,747,580,747)
    p.setFont('Helvetica', 12)
    p.drawString(60, 750,'Eu José Bernardo Luacute, Pastor da Igreja, certifico que '+nome+',')
    p.drawString(30, 735,'É membro dessa igreja com o numero de membro '+other.numeroDeMembro+' passado aos '+str(other.dataDeBaptismo)+'.')
    


    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response



def programa(request):

	if request.method=='POST':
		form = ProgramaForm(request.POST)
		if form.is_valid():


			new_configuracoes=Programa(diaDaSemana =form.cleaned_data['diaDaSemana'],descricao=form.cleaned_data['descricao'])
			new_configuracoes.save()
			return HttpResponseRedirect('/gestao/')
	else:
		form=ProgramaForm()
	template='inserirPrograma.html'
	return render(request,template,{'form':form})


"""def login(request):
	email = request.GET.get('email')
	password = request.GET.get('password')
	content =''
	if request.method =='GET':
		try:
			resultado = User.objects.filter(userEmail=email, userPassword=password)
			if resultado:
				return HttpResponseRedirect('/gestao/')
			else:
				content='Username e Password inválida'
		except IndexError:
				return HttpResponse('Log out')
	
	
	
	template = 'login.html'
	
	return render(request, template, {'content':content})


def pesquisarUser(email,password):
    query = connection.cursor()
    query.execute("select * from DjangoOnIis_user where userEmail = '' and userPassword=''" %(email, password));
    return dictfetchall(query) """


































