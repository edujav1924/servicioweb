from django.db import models
class Supervisor(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
             return '%s' % (self.nombre)
class Encargado(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField()
    def __str__(self):
             return '%s' % (self.nombre)
class pedido(models.Model):
    supervisor = models.ForeignKey(Supervisor)
    encargado = models.ForeignKey(Encargado)
    direccion = models.CharField(max_length=30)
    id_producto = models.IntegerField(unique=True)
    def __str__(self):
             return '%s %s %s %d' % (self.supervisor, self.encargado,self.direccion,self.id_producto)
