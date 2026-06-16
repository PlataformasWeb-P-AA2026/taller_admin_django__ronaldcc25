from django.contrib import admin

# Register your models here.
from institucion.models import Exhibicion, GuiaMuseo, Museo


class MuseoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ciudad", "anio_fundacion")
    search_fields = ("nombre", "ciudad")


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
