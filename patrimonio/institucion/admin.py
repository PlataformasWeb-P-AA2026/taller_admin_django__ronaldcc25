from django.contrib import admin

# Register your models here.
from institucion.models import Exhibicion, GuiaMuseo, Museo


class MuseoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "ciudad",
        "anio_fundacion",
        "costo_total_produccion",
        "guia_mas_experimentado",
    )
    search_fields = ("nombre", "ciudad")

    def costo_total_produccion(self, obj):
        return f"${obj.costo_total_produccion()}"

    costo_total_produccion.short_description = "Costo Total Producción"

    def guia_mas_experimentado(self, obj):
        return obj.guia_mas_experimentado()

    guia_mas_experimentado.short_description = "Guía más Experimentado"


class GuiaMuseoAdmin(admin.ModelAdmin):
    list_display = ("nombre_completo", "anios_experiencia_guia", "idiomas_hablados")
    search_fields = ("nombre_completo", "anios_experiencia_guia", "idiomas_hablados")


class ExhibicionAdmin(admin.ModelAdmin):
    list_display = (
        "titulo_exhibicion",
        "duracion_meses",
        "costo_produccion",
        "tematica",
    )
    search_fields = ("titulo_exhibicion", "tematica")


admin.site.register(Museo, MuseoAdmin)
admin.site.register(GuiaMuseo, GuiaMuseoAdmin)
admin.site.register(Exhibicion, ExhibicionAdmin)
