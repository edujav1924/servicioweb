from django.contrib import admin
from biblioteca.models import Supervisor,Encargado,pedido


class PedidosAdmin(admin.ModelAdmin):
    list_display = ('supervisor', 'encargado', 'id_producto','direccion')
admin.site.register(Supervisor)
admin.site.register(Encargado)
admin.site.register(pedido,PedidosAdmin)
    # Register your models here.
