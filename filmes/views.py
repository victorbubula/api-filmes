from rest_framework import viewsets, filters
from rest_framework import status
from filmes.models import Filme
from filmes.serializer import FilmeSerializer, FilmeSerializerV2
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

class FilmesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Filmes"""
    queryset = Filme.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'genero1', 'genero2']
    filterset_fields = ['assistido']
    http_method_names = ['get', 'post', 'put', 'path', 'delete']
    
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return FilmeSerializerV2
        else:
            return FilmeSerializer
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            id = str(serializer.data['id'])
            response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            response['Location'] = request.build_absolute_uri() + id
            return response