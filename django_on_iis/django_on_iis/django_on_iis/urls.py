from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^login/$', 'DjangoOnIis.views.login', name='login'),
    url(r'^gestao/$', 'DjangoOnIis.views.home', name='home'),
    url(r'^gestao/membro/editar/$', 'DjangoOnIis.views.editarMembro', name='editarMembro'),
    url(r'^gestao/membro/eliminar/$', 'DjangoOnIis.views.eliminarMembro', name='eliminarMembro'),
    url(r'^gestao/membro/visualizar/$', 'DjangoOnIis.views.visualizarMembro', name='visualizarMembro'),
    url(r'^gestao/membro/pesquisar/$', 'DjangoOnIis.views.pesquisarMembro', name='pesquisarMembro'),
    url(r'^gestao/membro/$' ,'DjangoOnIis.views.homeMembro', name='homeMembro'),
    url(r'^gestao/financas/contribuicao/$' ,'DjangoOnIis.views.contribuicao', name='contribuicao'),
    url(r'^gestao/financas/contribuicao/visualizar/$' ,'DjangoOnIis.views.visualizarContribuicao', name='visualizarContribuicao'),
    url(r'^gestao/financas/contribuicao/pesquisar/$' ,'DjangoOnIis.views.pesquisarContribuicao', name='pesquisarContribuicao'),
    url(r'^gestao/financas/contribuicao/editar/$' ,'DjangoOnIis.views.editarContribuicao', name='editarContribuicao'),
    url(r'^gestao/financas/contribuicao/eliminar/$' ,'DjangoOnIis.views.eliminarContribuicao', name='eliminarContribuicao'),
    url(r'^gestao/financas/ofertas/$' ,'DjangoOnIis.views.oferta', name='oferta'),
    url(r'^gestao/financas/ofertas/pesquisar/$' ,'DjangoOnIis.views.pesquisarOferta', name='pesquisarOferta'),
    url(r'^gestao/financas/projetos/$' ,'DjangoOnIis.views.projeto', name='projeto'),
    url(r'^gestao/financas/projetos/pesquisar/$' ,'DjangoOnIis.views.pesquisarProjecto', name='pesquisarProjecto'),
    url(r'^gestao/financas/projetos/editar/$' ,'DjangoOnIis.views.editarProjecto', name='editarProjecto'),
    url(r'^gestao/financas/projetos/eliminar/$' ,'DjangoOnIis.views.eliminarProjecto', name='eliminarProjecto'),
    url(r'^gestao/financas/dizimos/$' ,'DjangoOnIis.views.dizimo', name='dizimo'),
    url(r'^gestao/financas/dizimos/visualizar/$' ,'DjangoOnIis.views.visualizarDizimo', name='visualizarDizimo'),
    url(r'^gestao/financas/dizimos/editar/$' ,'DjangoOnIis.views.editarDizimo', name='editarDizimo'),
    url(r'^gestao/financas/dizimos/eliminar/$' ,'DjangoOnIis.views.eliminarDizimo', name='eliminarDizimo'),
    url(r'^gestao/financas/dizimos/total/$' ,'DjangoOnIis.views.totalValores', name='totalValores'),
    url(r'^gestao/rh/funcionario/$' ,'DjangoOnIis.views.funcionario', name='funcionario'),
    url(r'^gestao/rh/funcionario/pesquisar/$' ,'DjangoOnIis.views.pesquisarFuncionario', name='pesquisarFuncionario'),
    url(r'^gestao/rh/funcionario/salario/$' ,'DjangoOnIis.views.visualizarSalario', name='visualizarSalario'),
    url(r'^gestao/rh/funcionario/salario/inserir/$' ,'DjangoOnIis.views.inserirSalario', name='inserirSalario'),
    url(r'^gestao/rh/funcionario/salario/editar/$' ,'DjangoOnIis.views.EditarSalario', name='EditarSalario'),
    url(r'^gestao/rh/funcionario/salario/eliminar/$' ,'DjangoOnIis.views.eliminarSalario', name='eliminarSalario'),
    url(r'^gestao/rh/funcionario/visualizar/$' ,'DjangoOnIis.views.visualizarFuncionario', name='visualizarFuncionario'),
    url(r'^gestao/rh/funcionario/editar/$' ,'DjangoOnIis.views.editarFuncionario', name='editarFuncionario'),
    url(r'^gestao/rh/funcionario/eliminar/$' ,'DjangoOnIis.views.eliminarFuncionario', name='eliminarFuncionario'),
    url(r'^gestao/inventario/$' ,'DjangoOnIis.views.equipamento', name='equipamento'),
    url(r'^gestao/inventario/pesquisar/$' ,'DjangoOnIis.views.pesquisarEquipamento', name='pesquisarEquipamento'),
    url(r'^gestao/inventario/editar/$' ,'DjangoOnIis.views.editarEquipamento', name='editarEquipamento'),
    url(r'^gestao/inventario/eliminar/$', 'DjangoOnIis.views.eliminarEquipamento', name='eliminarEquipamento'),
    #url(r'^$','DjangoOnIis.views.base', name='base'),

     #Noticias e eventos --------------------------------------
         #Noticias e eventos --------------------------------------
     url(r'^gestao/noticias/$' ,'DjangoOnIis.views.indexNoticias', name='indexNoticias'),
     url(r'^gestao/noticias/lermais$' ,'DjangoOnIis.views.lerNoticias', name='lerNoticias'),
     #url(r'^gestao/noticias/visualizar$' ,'DjangoOnIis.views.visualizarNoticias', name='visualizarNoticias'),
     #url(r'^gestao/eventos$' ,'DjangoOnIis.views.eventos', name='eventos'),

     #____________________________________________________Reports_______________________________________________________________
     url(r'^gestao/noticias/publicar/$' ,'DjangoOnIis.views.publicarNoticia', name='publicarNoticia'),


     #HOME
     url(r'^$' ,'DjangoOnIis.views.home_site', name='home_site'),
     url(r'^gestao/homeum$' ,'DjangoOnIis.views.homeUm', name='homeUm'),




#CONFIGURAcoES
     url(r'^gestao/configuracoes/$' ,'DjangoOnIis.views.configuracoes', name='configuracoes'),
    url(r"^cartaDeRecomendacao.pdf$", 'DjangoOnIis.views.cartaDeRecomendacao', name='cartaDeRecomendacao'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),

    #) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


