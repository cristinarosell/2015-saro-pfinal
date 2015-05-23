from django.contrib import admin
from models import Evento, Usuario, EventosUsuario, FechaAct, Comentario, Votacion, Seguimiento

# Register your models here.

admin.site.register(Evento)
admin.site.register(Usuario)
admin.site.register(EventosUsuario)
admin.site.register(FechaAct)
admin.site.register(Comentario)
admin.site.register(Votacion)
admin.site.register(Seguimiento)
