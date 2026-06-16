from django.db import models

# Create your models here.


class Museo(models.Model):
    nombre = models.CharField(max_length=60, unique=True, null=False)
    ciudad = models.CharField(max_length=50)
    anio_fundacion = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.ciudad} - {self.anio_fundacion}"


class GuiaMuseo(models.Model):
    nombre_completo = models.CharField(max_length=120)
    anios_experiencia_guia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=100)
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_completo} - {self.anios_experiencia_guia} años exp - {self.idiomas_hablados}"


class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=100)
    duracion_meses = models.IntegerField()
    costo_produccion = models.DecimalField(max_digits=10, decimal_places=2)
    tematica = models.CharField(max_length=100)
    guia = models.ForeignKey(GuiaMuseo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo_exhibicion} - {self.tematica} - Asistida por: {self.guia.nombre_completo}"
