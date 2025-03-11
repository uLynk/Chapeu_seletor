from django.contrib import admin
from .models import Pergunta, Resposta, Casa, Usuario, Time, Partida

admin.site.register(Pergunta)
admin.site.register(Resposta)
admin.site.register(Casa)
admin.site.register(Usuario)
admin.site.register(Time)
admin.site.register(Partida)