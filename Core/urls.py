from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index, name='Index'),
    path('<int:car_id>',views.Detalhes, name='Detalhes'),
    path('Veiculos',views.Consecionaria,name='Veiculos'),
    path('Cadastrar',views.Cadastrar,name='Cadastrar'),
    path('Buscar', views.Buscar, name='Buscar'),
    path('Marcas',views.CadstMarca,name='Marcas'),
]