from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),#admin
    path('', views.index, name='index'), # ruta del index
    path('', include('Dashboard.urls')), #inclusion de rutas de la app dashboard 
    path('', include('Login_Users.urls')), #inclusion de rutas de la app login_users
    path('', include('Clientes_Mascotas.urls')), #inclusion de rutas de la app clientes_mascotas
    path('', include('Historiales_clinicos.urls')), #inclusion de rutas de la app historiales_clinicos

]

