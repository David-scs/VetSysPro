from django.urls import path
from . import views

urlpatterns = [
    path('vista__mascota/<int:idMascota>/', views.vista_mascota, name='vista__mascota'),
    path('listar_consulta/<int:idMascota>/', views.listar_consulta, name='listar_consulta'),
    path('detalles_consulta/<int:idConsulta>/', views.detalles_consulta, name='detalles_consulta'),
    path('registrar_consulta/', views.registrar_consulta, name='registrar_consulta'),
    path('listar_vacunas/<int:idMascota>/', views.listar_vacunas, name='listar_vacunas'),
    path('registrar_vacuna/', views.registrar_vacuna, name='registrar_vacuna'),
    path('guardar_archivo_mascota/', views.guardar_archivo_mascota, name='guardar_archivo_mascota'),
    path('listar_desparasitantes/<int:idMascota>/', views.listar_desparacitantes, name='listar_desparacitantes'),
    path('registrar_desparasitante/', views.registrar_desparasitante, name='registrar_desparasitante'),
    path('listar_archivos/<int:idMascota>/', views.listar_archivos, name='listar_archivos'),
    path('cargar_archivo/', views.cargar_archivo, name='cargar_archivo'),
]
    
