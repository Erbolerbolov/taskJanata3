from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .permission import IsAdminOrAlloAny

from .models import Category
from .serializers import CategorySerializer


class ListCreateCategoryView(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrAlloAny, )