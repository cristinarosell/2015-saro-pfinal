from django.db import models

# Create your models here.

class Evento (models.Model):
    identif = models.IntegerField()
    titulo = models.CharField(max_length = 64)
    tipo = models.CharField(max_length = 150)
    comentprecio = models.CharField(max_length = 64)
    precio =  models.FloatField()
    fechahora = models.DateTimeField()
    duracion = models.FloatField()
    largaduracion = models.BooleanField()
    url = models.CharField(max_length = 150)
    descripcion = models.CharField(max_length = 300)
    
class FechaAct (models.Model):
    fecha = models.DateTimeField()
    
class Usuario (models.Model):
    nombre = models.CharField(max_length = 32)
    npag = models.CharField(max_length = 32)
    descrpag = models.CharField(max_length = 150, default= "vacio")
    tamanoletra = models.CharField(max_length = 32, default= "small")
    colorletra = models.CharField(max_length = 32, default= "black")
    colorfondo = models.CharField(max_length = 32, default= "white")
    imagenbanner = models.CharField(max_length = 32, default= "Madrid3.jpg")
    
class EventosUsuario (models.Model):
    evento = models.ForeignKey(Evento)
    usuario = models.ForeignKey(Usuario)
    fechareg = models.DateTimeField()
    
class Comentario (models.Model):
    texto = models.CharField(max_length = 300, default = "vacio")
    evento = models.ForeignKey(Evento)
    usuario = models.ForeignKey(Usuario)
    fechacom = models.DateTimeField()
    
class Votacion (models.Model):
    puntuacion = models.IntegerField()
    evento = models.ForeignKey(Evento)
    
class Seguimiento (models.Model):
    usuario = models.ForeignKey(Usuario)
    usuarioseguido = models.ForeignKey(Usuario, related_name = "seguido")
    
    

