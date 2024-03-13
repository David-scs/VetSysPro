from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard(request):
    current_page = "dashboard"  # Definimos la página actual como "dashboard"
    return render(request, 'dashboard.html', {'current_page': current_page})