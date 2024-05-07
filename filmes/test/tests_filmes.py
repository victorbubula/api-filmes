from rest_framework.test import APITestCase
from filmes.models import Filme
from django.urls import reverse

class FilmesTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Filmes-list')
        self.filme_1 = Filme.objects.create(
            nome='CTT1', tipo='F', genero1='Ac', genero2='Av', genero3='Ac', imagem='awdkwajdkwajd'
        )
        self.filme_2 = Filme.objects.create(
            nome='CTT2', tipo='S', genero1='C', genero2='D', genero3='Fan', imagem='awdkwawdqwqdwqdqdqjdkwajd'
        )

    def test_falhador(self):
        self.fail('Teste falhou de proposido, noa se preocupe')