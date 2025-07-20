from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('comprar/', views.comprar_view, name='comprar'),
    path('vendas/', views.inicio_view, name='inicio'),
    path('consultar/', views.consultar_view, name='consultar'),
    path('api/produto/<int:produto_id>/', views.encontrar_dados_produto, name='encontrar_dados_produto'),
]
