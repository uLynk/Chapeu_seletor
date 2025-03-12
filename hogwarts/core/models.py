from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Casa(models.Model):
    nome = models.CharField(max_length=100)
    cor_primaria = models.CharField(max_length=7)
    cor_secundaria = models.CharField(max_length=7)
    diretor = models.CharField(max_length=100, null=True, blank=True) 
    mensagem_diretor = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Usuario(AbstractUser):
    casa = models.ForeignKey(Casa, null=True, blank=True, on_delete=models.SET_NULL)

class Pergunta(models.Model):
    texto = models.CharField(max_length=255)

    def __str__(self):
        return self.texto

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, related_name='respostas', on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)
    casa = models.ForeignKey('Casa', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.texto} ({self.casa.nome})"
    
class Time(models.Model):
    nome = models.CharField(max_length=100)
    pontos = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class Partida(models.Model):
    time1 = models.ForeignKey(Time, related_name="time1", on_delete=models.CASCADE)
    time2 = models.ForeignKey(Time, related_name="time2", on_delete=models.CASCADE)
    placar_time1 = models.IntegerField()
    placar_time2 = models.IntegerField()
    data = models.DateField()

    def __str__(self):
        return f"{self.time1} vs {self.time2} - {self.data}"