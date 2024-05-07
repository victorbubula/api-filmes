from django.contrib import admin
from filmes.models import Filme

class Filmes(admin.ModelAdmin):
    list_display = ('id','nome', 'tipo', 'genero1','genero2', 'assistido' )
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'genero1', 'genero2')
    list_filter = ('assistido',)
    list_editable = ('assistido',)
    list_per_page = 15
    ordering = ('nome',)

admin.site.register(Filme, Filmes)
