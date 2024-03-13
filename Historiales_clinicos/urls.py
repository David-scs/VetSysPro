from django.urls import path
from . import views

urlpatterns = [
    path('vista__mascota/<int:idMascota>/', views.vista_mascota, name='vista__mascota'),
    path('listar_consulta/<int:idMascota>/', views.listar_consulta, name='listar_consulta'),
    path('detalles_consulta/<int:idConsulta>/', views.detalles_consulta, name='detalles_consulta'),
    path('registrar_consulta/', views.registrar_consulta, name='registrar_consulta'),
    path('listar_vacunas/<int:idMascota>/', views.listar_vacunas, name='listar_vacunas'),
    
]