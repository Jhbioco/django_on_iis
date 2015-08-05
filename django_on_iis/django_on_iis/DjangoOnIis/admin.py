from django.contrib import admin
from .models import Pais,Provincia,Municipio,Igreja,Departamento,Membro
# Register your models here.
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Municipio)
admin.site.register(Igreja)
admin.site.register(Departamento)
admin.site.register(Membro)