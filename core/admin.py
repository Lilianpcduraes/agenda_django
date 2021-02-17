from django.contrib import admin
from core.models import Evento
# Register your models here.

#o segue código para mostrar os dados que eu quero
class EventoAdmin (admin.ModelAdmin):
    list_display = ('titulo','data_evento', 'data_criacao')
 #Temos que associar o even'to a classe no registro. Se eu esquecer não aparecerá a alterção
    list_filter = ('usuario','data_evento',)#tem que colocar a virgula no final
admin.site.register(Evento, EventoAdmin)