from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Propietario, Mascota, EstadoReproductivo
from django.shortcuts import get_object_or_404
from django.contrib import messages


@login_required
def listar_propietarios(request):
    propietarios = Propietario.objects.all()
    current_page = "consultorio" 
    return render(request, 'consultorio.html', {'propietarios': propietarios, 'current_page': current_page})

@login_required
def registrar_propietario(request):
    documento = request.POST.get('txtDocumentoP')
    nombres = request.POST.get('txtNombreP')
    apellidos = request.POST.get('txtApellidosP')
    direccion = request.POST.get('txtDireccionP')
    email = request.POST.get('txtEmailP')
    telefono = request.POST.get('txtTelP')
    nombreEmer = request.POST.get('txtNombreE')
    telefonoEmer = request.POST.get('txtTelE')
    
    propietario = Propietario.objects.create(documento=documento, nombres=nombres, apellidos=apellidos, direccion=direccion, email=email, telefono=telefono, nombreEmer=nombreEmer, telefonoEmer=telefonoEmer)
    propietario = Propietario.objects.get(documento=documento)
    
    
    return render(request, 'Perfil_propietario.html', {'propietario':propietario} )

#redireccionar a la pagina de perfil del propietario y mostrar la informacion del propietario
@login_required
def Perfil_Propietario(request, documento):
    
    current_page = "consultorio" 
    estados = EstadoReproductivo.objects.all()
    propietarios = Propietario.objects.all()
    propietario = Propietario.objects.get(documento=documento)
    mascotas = Mascota.objects.filter(propietario=propietario)
    
    return render(request, 'Perfil_propietario.html', {'propietario': propietario, 'estados': estados, 'propietarios': propietarios, 'mascotas': mascotas, 'current_page': current_page})

@login_required
def eliminar_propietario(request, documento):
    propietario = Propietario.objects.get(documento=documento)
    propietario.delete()
    return redirect('consultorio')

#Actualizar propietario
@login_required
def actualizar_propietario(request, documento):
    if request.method == 'POST':
        nombres = request.POST.get('txtNombreP')
        apellidos = request.POST.get('txtApellidosP')
        direccion = request.POST.get('txtDireccionP')
        email = request.POST.get('txtEmailP')
        telefono = request.POST.get('txtTelP')
        nombreEmer = request.POST.get('txtNombreE')
        telefonoEmer = request.POST.get('txtTelE')
        
        propietario = get_object_or_404(Propietario, documento=documento)
        propietario.nombres = nombres
        propietario.apellidos = apellidos
        propietario.direccion = direccion
        propietario.email = email
        propietario.telefono = telefono
        propietario.nombreEmer = nombreEmer
        propietario.telefonoEmer = telefonoEmer
        propietario.save()
        return redirect('consultorio')
    
@login_required
def Registrar_Mascota(request):
    
    estados = EstadoReproductivo.objects.all()
    
    idMascota = request.POST.get('txtIdMascota')
    foto = request.POST.get('txtFoto')
    nombre = request.POST.get('txtNombreMascota')
    especie = request.POST.get('txtEspecie')
    raza = request.POST.get('txtRaza')
    sexo = request.POST.get('txtSexo')
    color = request.POST.get('txtColor')
    edad = request.POST.get('txtEdad')
    peso = request.POST.get('txtPeso')
    personalidad = request.POST.get('txtPersonalidad')
    tipoalimentacion = request.POST.get('txtAlimentacion')
    cantidadAlimento = request.POST.get('txtCantidadAlimento')
    frecuenciaAlimentacion = request.POST.get('txtFrecuenciaAlimentacion')
    frecuenciaBano = request.POST.get('txtFrecuenciaBano')
    antecedentesClinicos = request.POST.get('txtAntecedentesClinicos')
    propietario = request.POST.get('txtPropietario')
    Estados = request.POST.get('txtEstadoReproductivo')
    
    propietario = Propietario.objects.get(pk=propietario)
    estados = EstadoReproductivo.objects.get(pk=Estados)

    mascota = Mascota.objects.create(idMascota=idMascota, foto=foto, nombre=nombre, especie=especie, raza=raza, sexo=sexo, color=color, edad=edad, peso=peso, personalidad=personalidad, tipoalimentacion=tipoalimentacion, cantidadAlimento=cantidadAlimento, frecuenciaAlimentacion=frecuenciaAlimentacion, frecuenciaBano=frecuenciaBano, antecedentesClinicos=antecedentesClinicos, propietario=propietario, EstadoReproductivo=estados)
    return redirect('/Perfil_propietario/{}/'.format(propietario.documento))
    