from django.db import models
from Clientes_Mascotas.models import Mascota
from datetime import date

from django.db import models
from datetime import date

from django.db import models
from datetime import date

class Consulta(models.Model):
    fecha = models.DateField(default=date.today)
    motivo = models.CharField(max_length=100)
    detalles = models.TextField()
    prueba_diagnostica = models.TextField()
    diagnostico_diferencial = models.CharField(max_length=100)
    diagnostico_definitivo = models.CharField(max_length=100)
    pronostico = models.CharField(max_length=100)
    seguimiento = models.CharField(max_length=100)
    temperatura_corporal = models.DecimalField(max_digits=5, decimal_places=2)
    frecuencia_cardiaca = models.PositiveSmallIntegerField()
    peso_examen = models.DecimalField(max_digits=5, decimal_places=2)
    observaciones_examen = models.TextField()
    receta_medica = models.TextField()
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Formatear la fecha como YYYY-MM-DD antes de guardarla
        self.fecha = self.fecha.strftime('%Y-%m-%d')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Consulta de {self.mascota.nombre}"


class Vacuna(models.Model):
    fecha = models.DateField(default=date.today)
    nombre = models.CharField(max_length=100)
    dosis = models.PositiveSmallIntegerField()
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

    def __str__(self):
        return f"Vacuna de {self.mascota.nombre}"
    
    
class desparasitantes(models.Model):
    fecha = models.DateField(default=date.today)
    nombre = models.CharField(max_length=100)
    dosis = models.PositiveSmallIntegerField()
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

    def __str__(self):
        return f"Desparasitante de {self.mascota.nombre}"