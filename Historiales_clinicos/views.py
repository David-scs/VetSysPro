from django.shortcuts import render, redirect
from Clientes_Mascotas.models import Mascota
from .models import Consulta, Vacuna, desparasitantes
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db import transaction

# Create your views here.
@login_required
def vista_mascota(request, idMascota):
    mascota = Mascota.objects.get(idMascota=idMascota)
    current_page = "consultorio" 
    current_page2 = "vista__mascota"
    return render(request, 'perfil_mascota.html', {'mascota': mascota, 'current_page': current_page, 'current_page2': current_page2})

from .models import Consulta, Mascota

def listar_consulta(request, idMascota):
    mascota = Mascota.objects.get(idMascota=idMascota)
    current_page = "consultorio" 
    current_page2 = "listar_consulta"
    
    # Filtrar las consultas por la mascota específica
    consultas = Consulta.objects.filter(mascota=mascota)
    fecha_actual = date.today()
    return render(request, 'listar_consulta.html', {'consultas': consultas, 'current_page': current_page, 'current_page2': current_page2,'mascota': mascota,'fecha_actual': fecha_actual})

def registrar_consulta(request):
    
    motivo = request.POST.get('motivoConsulta')
    detalles = request.POST.get('detallesConsulta')
    prueba_diagnostica = request.POST.get('pruebaDiagnosticaConsulta')
    diagnosico_diferencial = request.POST.get('diagnosticoDiferencial')
    diagnostico_definitivo = request.POST.get('diagnosticoDefinitivo')
    pronostico = request.POST.get('pronosticoConsulta')
    seguimiento = request.POST.get('seguimientoConsulta')
    temperatura_corporal = request.POST.get('temperaturaCorporalConsulta')
    frecuencia_cardiaca = request.POST.get('frecuenciaCardiacaConsulta')
    peso_examen = request.POST.get('pesoExamenConsulta')
    observaciones_examen = request.POST.get('observaciones_examen')
    receta_medica = request.POST.get('recetaMedicaConsulta')
    idMascota = request.POST.get('idMascota')
    
    mascota = Mascota.objects.get(idMascota=idMascota)
    
    consulta = Consulta.objects.create( motivo=motivo, detalles=detalles, prueba_diagnostica=prueba_diagnostica, diagnostico_diferencial=diagnosico_diferencial, diagnostico_definitivo=diagnostico_definitivo, pronostico=pronostico, seguimiento=seguimiento, temperatura_corporal=temperatura_corporal, frecuencia_cardiaca=frecuencia_cardiaca, peso_examen=peso_examen, observaciones_examen=observaciones_examen, receta_medica=receta_medica, mascota=mascota)
    return redirect('/listar_consulta/{}/'.format(idMascota))

def detalles_consulta(request, idConsulta):
    consulta = Consulta.objects.get(id=idConsulta)
    mascota = consulta.mascota  
    current_page = "consultorio" 
    current_page2 = "listar_consulta"
    return render(request, 'detalles_consulta.html', {'consulta': consulta, 'mascota': mascota, 'current_page': current_page, 'current_page2': current_page2})

def Mostrar_historial(request, idMascota):
    mascota = Mascota.objects.get(idMascota=idMascota)
    current_page = "consultorio" 
    current_page2 = "Mostrar_historial"
    return render(request, 'Mostrar_historial.html', {'mascota': mascota, 'current_page': current_page, 'current_page2': current_page2})

def listar_vacunas(request, idMascota):
    mascota = Mascota.objects.get(idMascota=idMascota)
    vacuna = Vacuna.objects.filter(mascota=mascota)
    current_page = "consultorio" 
    current_page2 = "listar_vacunas"
    return render(request, 'listar_vacunas.html', {'vacuna': vacuna,'mascota': mascota, 'current_page': current_page, 'current_page2': current_page2})


def registrar_vacuna(request):
    fecha = request.POST.get('fecha')
    nombre = request.POST.get('nombre')
    dosis = request.POST.get('dosis')
    idMascota = request.POST.get('idMascota')
    
    mascota = Mascota.objects.get(idMascota=idMascota)
    vacuna = Vacuna.objects.create(fecha=fecha, nombre=nombre, dosis=dosis, mascota=mascota)
    return redirect('/listar_vacunas/{}/'.format(idMascota))


def guardar_archivo_mascota(request):
    if request.method == 'POST' and request.FILES['archivo']:
        archivo = request.FILES['archivo']
        mascota_id = request.POST.get('mascota_id')  # Obtén el ID de la mascota desde el formulario
        mascota = Mascota.objects.get(idMascota=mascota_id)
        mascota.foto = archivo
        mascota.save() 
        current_page = "consultorio" 
        current_page2 = "vista__mascota"
        return render(request, 'perfil_mascota.html', {'mascota': mascota, 'current_page': current_page, 'current_page2': current_page2})

def listar_desparacitantes(request, idMascota):
    mascota = Mascota.objects.get(idMascota=idMascota)
    desparasitante = desparasitantes.objects.filter(mascota=mascota)
    current_page = "consultorio" 
    current_page2 = "listar_desparacitantes"
    return render(request, 'listar_desparasitantes.html', {'mascota': mascota, 'current_page': current_page, 'current_page2': current_page2, 'desparasitantes': desparasitante})

def registrar_desparasitante(request):
    fecha = request.POST.get('fecha')
    nombre = request.POST.get('nombre')
    dosis = request.POST.get('dosis')
    idMascota = request.POST.get('idMascota')
    
    mascota = Mascota.objects.get(idMascota=idMascota)
    desparasitante = desparasitantes.objects.create(fecha=fecha, nombre=nombre, dosis=dosis, mascota=mascota)
    return redirect('/listar_desparasitantes/{}/'.format(idMascota))