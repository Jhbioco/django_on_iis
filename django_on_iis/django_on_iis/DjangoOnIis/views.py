from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
from .models import Pais,Provincia, Municipio, Igreja, Departamento, Membro
#from .forms import IgrejaForm
from django.db import connection
from .forms import MembroForm

# Create your views here.

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

def indexAdmin(request):
	dados = {}
	template = 'indexAdmin.html'
	return render(request,template,dados)

def inserirMembro(request):


	valor = request.GET.get('id')
	if valor: 
		resultado = get_editar_membro(valor)
		print "ola"
		print resultado[0]['nomeDoMembro']

	#return valor


	if request.method == 'POST':
		form = MembroForm(request.POST)
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
			

			new_membro, created = Membro.objects.get_or_create(nomeDoMembro=nomeDoMembro, estadoCivil=estadoCivil, sexo=sexo,
				cargo = cargo, funcaoNaIgreja=funcaoNaIgreja, endereco=endereco, bairro=bairro, provincia=provincia, caixaPostal=caixaPostal,
				telefone=telefone, email=email, dataDeNascimento=dataDeNascimento, pais=pais, grauAcademico=grauAcademico,
				profissao=profissao, numeroDeIdentificacao=numeroDeIdentificacao, conjuge=conjuge, filiacaoPai=filiacaoPai,
				filiacaoMae=filiacaoMae, dataDeConversao=dataDeConversao, procedencia=procedencia, formaDeAdmissao= formaDeAdmissao,
				dataDeBaptismo=dataDeBaptismo, localDeBaptismo=localDeBaptismo, dataDeConsagracaoDiacono= dataDeConsagracaoDiacono,
				dataDeConsagracaoEvangelista= dataDeConsagracaoEvangelista, dataDeConsagracaoPastor=dataDeConsagracaoPastor,
				dataDeConsagracaoMissionario=dataDeConsagracaoMissionario, departamento=departamento,igreja=igreja,
				numeroDeMembro=numeroDeMembro)
	else:
		form = MembroForm()

	provincia = Provincia.objects.all()
	pais = Pais.objects.all()
	departamento=Departamento.objects.all()
	igreja = Igreja.objects.all()

	return render(request, 'inserirMembros.html',{'form':form,'provincia':provincia,'pais':pais,'departamento':departamento,'igreja':igreja})



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


def pesquisarMembro(request):

	content =''
	opcao = request.GET.get('opcao')
	informacao = request.GET.get('informacao')
	print informacao
	print opcao
	if opcao == 'Nome':
		resultado = get_nome(informacao)
		content ={'query':opcao, 'resultado':resultado}
	elif opcao == 'Numero_de_Membro':
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
		form = MembroForm(request.POST)
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

			

			created = Membro.objects.filter(pk=valor).update(nomeDoMembro=nomeDoMembro, estadoCivil=estadoCivil, sexo=sexo,
				cargo = cargo, funcaoNaIgreja=funcaoNaIgreja, endereco=endereco, bairro=bairro, provincia=provincia, caixaPostal=caixaPostal,
				telefone=telefone, email=email, dataDeNascimento=dataDeNascimento, pais=pais, grauAcademico=grauAcademico,
				profissao=profissao, numeroDeIdentificacao=numeroDeIdentificacao, conjuge=conjuge, filiacaoPai=filiacaoPai,
				filiacaoMae=filiacaoMae, dataDeConversao=dataDeConversao, procedencia=procedencia, formaDeAdmissao= formaDeAdmissao,
				dataDeBaptismo=dataDeBaptismo, localDeBaptismo=localDeBaptismo, dataDeConsagracaoDiacono= dataDeConsagracaoDiacono,
				dataDeConsagracaoEvangelista= dataDeConsagracaoEvangelista, dataDeConsagracaoPastor=dataDeConsagracaoPastor,
				dataDeConsagracaoMissionario=dataDeConsagracaoMissionario, departamento=departamento,igreja=igreja,
				numeroDeMembro=numeroDeMembro)
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









