from django.urls import path
from . import views

urlpatterns = [
    path('consultorio/', views.listar_propietarios, name='consultorio'),
    path('registrar_propietario/', views.registrar_propietario,name='registrar_propietario'),
    path('Perfil_propietario/<int:documento>/', views.Perfil_Propietario , name='Perfil_propietario'),
    path('eliminar_propietario/<int:documento>/', views.eliminar_propietario, name='eliminar_propietario'),
    path('actualizar_propietario/<int:documento>/', views.actualizar_propietario, name='actualizar_propietario'),
    path('registrar_mascota/', views.Registrar_Mascota, name='registrar_mascota'),
]
