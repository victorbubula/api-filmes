from django.contrib import admin
from django.urls import path, include
from filmes.views import FilmesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('filmes', FilmesViewSet, basename='Filmes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
]