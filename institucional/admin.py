from django.contrib import admin
from .models import Inicio, Contato

class InicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'link', 'id') 
    list_filter = ('titulo', 'link', 'id')

admin.site.register(Inicio, InicioAdmin)
admin.site.register(Contato)