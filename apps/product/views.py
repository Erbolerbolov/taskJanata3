from rest_framework import generics
from .models import Product
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import ProductSerializer
from .paginations import ProductPagination


class ListCreateProductView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_published', 'title']

    # def get_queryset(self):
    #     return Product.objects.filter(is_published=True)
    def get_serializer_context(self):
        return super().get_serializer_context()
        