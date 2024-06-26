from rest_framework import serializers
from filmes.models import Filme

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['id','nome','tipo','genero1','genero2','assistido']

class FilmeSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'