from rest_framework import viewsets, filters
from filmes.models import Filme
from filmes.serializer import FilmeSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class FilmesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Filmes"""
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'genero1', 'genero2']
    filterset_fields = ['assistido']
