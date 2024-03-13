from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Propietario (models.Model):
    documento = models.CharField(max_length=10, primary_key=True , null=False, unique=True)
    nombres = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=80, null=False)
    email = models.EmailField(max_length=50, null=False)
    telefono = models.CharField(max_length=10, null=False)
    nombreEmer= models.CharField(max_length=50, null=False)
    telefonoEmer = models.CharField(max_length=10, null=False)
    
class EstadoReproductivo (models.Model):
    idEstadoReproductivo = models.AutoField(primary_key=True)
    Estado = models.CharField(max_length=50)

class Mascota (models.Model):
    idMascota = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='fotos_mascotas', null=True, blank=True)
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    color = models.CharField(max_length=20)
    edad = models.CharField(max_length=20)
    peso = models.CharField(max_length=20)
    personalidad = models.CharField(max_length=100)
    tipoalimentacion = models.CharField(max_length=100)
    cantidadAlimento = models.CharField(max_length=100)
    frecuenciaAlimentacion = models.CharField(max_length=100)
    frecuenciaBano = models.CharField(max_length=100)
    antecedentesClinicos = models.CharField( max_length=100,null=True)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    EstadoReproductivo = models.ForeignKey(EstadoReproductivo, on_delete=models.CASCADE)
    
    def actualizar_foto(self, nueva_foto):
        self.foto = nueva_foto
        self.save()
        
