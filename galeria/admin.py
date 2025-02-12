from django.contrib import admin
from galeria.models import Fotografia

class FotografiasAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada", "data_fotografia")
    list_editable = ("publicada",)
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_per_page = 25

admin.site.register(Fotografia, FotografiasAdmin)
