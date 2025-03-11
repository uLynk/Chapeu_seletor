from django.urls import path
from . import views
from .views import logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),

    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    
    path('chapeu-seletor/', views.chapeu_seletor, name='chapeu_seletor'),
    path('processar-chapeu/', views.processar_chapeu, name='processar_chapeu'),
    path('minha-casa/', views.minha_casa, name='minha_casa'),
    
    path('beco_diagonal/', views.beco_diagonal, name='beco_diagonal'),
    path('quadribol/', views.quadribol, name='quadribol'),
    path('casa/', views.casa, name='casa'),

]
