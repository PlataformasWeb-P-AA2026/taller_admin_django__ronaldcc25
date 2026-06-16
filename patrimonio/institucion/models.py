from django.db import models

# Create your models here.


class Museo(models.Model):
    nombre = models.CharField(max_length=60, unique=True, null=False)
    ciudad = models.CharField(max_length=50)
    anio_fundacion = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.ciudad} - {self.anio_fundacion}"

    def costo_total_produccion(self):
        """Calcula el costo total de todas las exhibiciones del museo"""
        total = 0
        guias = self.guiamuseo_set.all()
        for guia in guias:
            exhibiciones = guia.exhibicion_set.all()
            for exhibicion in exhibiciones:
                total += exhibicion.costo_produccion
        return total

    def guia_mas_experimentado(self):
        guias = self.guiamuseo_set.all()
        if not guias:
            return "Sin guías"

        # Encontrar el máximo de experiencia
        max_experiencia = max(guia.anios_experiencia_guia for guia in guias)

        # Filtrar guías con experiencia máxima
        guias_max = [
            guia for guia in guias if guia.anios_experiencia_guia == max_experiencia
        ]

        # Retornar nombres concatenados
        nombres = ", ".join(guia.nombre_completo for guia in guias_max)
        return nombres


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
