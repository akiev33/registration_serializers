from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from categories.models import Category

from categories.serializers import CategorySerializers


class CategoryPagination(PageNumberPagination):
    page_size = 2


class CategoryAPIView(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    pagination_class = CategoryPagination