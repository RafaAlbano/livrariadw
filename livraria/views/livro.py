from rest_framework.viewsets import ModelViewSet

from livraria.models import Livro
from livraria.serializers import LivroDetailSerializer, LivroSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LivroDetailSerializer
        return LivroSerializer