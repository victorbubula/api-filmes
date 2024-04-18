from rest_framework import viewsets, filters
from filmes.models import Filme
from filmes.serializer import FilmeSerializer, FilmeSerializerV2
from django_filters.rest_framework import DjangoFilterBackend

class FilmesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Filmes"""
    queryset = Filme.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'genero1', 'genero2']
    filterset_fields = ['assistido']
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return FilmeSerializerV2
        else:
            return FilmeSerializer