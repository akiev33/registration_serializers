from rest_framework import viewsets

from categories.models import Category

from categories.serializers import CategorySerializers


class CategoryAPIView(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()