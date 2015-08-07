from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^gestao/membro/$', 'DjangoOnIis.views.inserirMembro', name='inserirMembro'),
<<<<<<< HEAD
    url(r'^gestao/membro/pesquisar/$', 'DjangoOnIis.views.pesquisarMembro', name='pesquisarMembro'),
=======
     url(r'^gestao/membro/pesquisar/$', 'DjangoOnIis.views.pesquisarMembro', name='pesquisarMembro'),
>>>>>>> 241affb4339b95377c2c188aa107a2874dbfe72b
    url(r'^gestao/$' ,'DjangoOnIis.views.indexAdmin', name='indexAdmin'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
