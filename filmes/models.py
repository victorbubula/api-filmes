from django.db import models

class Filme(models.Model):
    GENEROS = (
        ('Ac', 'Ação'),
        ('Av', 'Aventura'),
        ('C', 'Comédia'),
        ('D', 'Drama'),
        ('Fan', 'Fantasia'),
        ('Fic', 'Ficção cientifica'),
        ('M', 'Mistério'),
        ('R', 'Romance'),
        ('T', 'Terror')
    )

    TIPO = (
        ('F', 'Filme'),
        ('S', 'Série')
    )

    nome = models.CharField(max_length=30, unique=True)
    tipo = models.CharField(max_length=1, choices=TIPO, blank=False, null=False, default='F')
    genero1 = models.CharField(max_length=3, choices=GENEROS, blank=False, null=False, default='Ac')
    genero2 = models.CharField(max_length=3, choices=GENEROS, blank=False, null=False, default='Av')
    genero3 = models.CharField(max_length=3, choices=GENEROS, blank=False, null=False, default='C')
    imagem = models.ImageField()
    assistido = models.BooleanField(default='False')

    def __str__(self):
        return self.nome