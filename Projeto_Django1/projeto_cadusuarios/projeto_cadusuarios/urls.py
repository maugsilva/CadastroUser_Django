from django.urls import path
from app_cadastrouser import views
urlpatterns = [
    #Rota, View responsável, nome de referência
    #usuarios.com
    path('',views.home,name='home'),
    #Criando a rota p/ usuarios da página do link local
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
