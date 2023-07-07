# from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from livraria.models import Autor, Categoria, Editora, Livro
from livraria.serializers import AutorSerializer, CategoriaSerializer, EditoraSerializer, LivroSerializer, LivroDetailSerializer



class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrive"]:
            return LivroDetailSerializer
        return LivroSerializer

