from django.db import models

#Criando o banco de dados
class Usuario(models.Model):
  id_usuarios = models.AutoField(primary_key=True)
  nome = models.TextField(max_length=255)
  idade = models.IntegerField()
