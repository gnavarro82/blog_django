from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

#Clase para crear importar exportar
class CategoriaResource(resources.ModelResource):
	class Meta:
		model = Categoria

#recibe 2 herencias
class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	search_fields=['nombre']#barra de busqueda
	list_display = ('nombre','estado','fecha_creacion')
	resources_class = CategoriaResource


class AutorResource(resources.ModelResource):
	class Meta:
		model = Autor

class AutoraAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	search_fields=['nombres','apellidos','correo']#barra de busqueda
	list_display = ('nombres','apellidos','correo','estado','fecha_creacion')
	resources_class = AutorResource

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutoraAdmin)
admin.site.register(Post)