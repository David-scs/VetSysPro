from . import views 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# funcion que renderiza el index de la aplicacion
def index(request):
    return render(request, 'index.html')

@login_required
def base_view(request):
    current_page = "dashboard"  # Puedes obtener este valor de acuerdo a la página actual o URL
    return render(request, 'base.html', {'current_page': current_page})

