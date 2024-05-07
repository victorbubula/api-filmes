from rest_framework.test import APITestCase
from filmes.models import Filme
from django.urls import reverse
from rest_framework import status

class FilmesTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Filmes-list')
        self.filme_1 = Filme.objects.create(
            nome='CTT1', tipo='F', genero1='Ac', genero2='Av', assistido=False
        )
        self.filme_2 = Filme.objects.create(
            nome='CTT2', tipo='S', genero1='Av', genero2='C', assistido=False
        )

    def test_requisicao_get_para_listar_filmes(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_post_para_criar_filmes(self):
        data = {
            'nome': 'CTT3',
            'tipo': 'F',
            'genero1': 'Ac',
            'genero2': 'Av',
            'assistido': 'False'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_filmes(self):
        response = self.client.delete('/filmes/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_alterar_filmes(self):
        data = {
            'nome': 'CTT2',
            'tipo': 'S',
            'genero1': 'Av',
            'genero2': 'C',
            'assistido': 'True'
        }
        response = self.client.put('/filmes/2/',data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)