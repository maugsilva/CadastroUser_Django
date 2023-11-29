from django.shortcuts import render
from .models import Usuario

def home(request):
  return render(request,'usuarios/home.html')
#Criando a view usuarios
def usuarios(request):
  #Salvar os dados da tela para o Banco de Dados
  novo_usuario = Usuario()
  novo_usuario.nome = request.POST.get('nome')
  novo_usuario.idade = request.POST.get('idade')
  novo_usuario.save()
  #Exibir todos os usuários ja cadastrados em uma nova página
  usuarios = {
    'usuarios': Usuario.objects.all()
  }
  
  #Retornar os dados para a página de 'Listagem de Usuários'
  return render(request,'usuarios/usuarios.html',usuarios)