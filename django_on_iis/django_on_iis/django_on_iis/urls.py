from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^gestao/membro/$', 'DjangoOnIis.views.inserirMembro', name='inserirMembro'),
     url(r'^gestao/membro/pesquisar/$', 'DjangoOnIis.views.pesquisarMembro', name='pesquisarMembro'),
    url(r'^gestao/$' ,'DjangoOnIis.views.indexAdmin', name='indexAdmin'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
