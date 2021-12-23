from rest_framework import viewsets
from products.permission import IsOwnerOrReadOnly
from products.serializers import ProductSerializers
from products.models import Product
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status

from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 10


class ProductAPIView(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    pagination_class = ProductPagination


    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        t = request.query_params.get('t')
        queryset = self.queryset.filter(
            Q(name__icontains=t) |
            Q(description__icontains=t)
        )
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def price(self, request, pk=None):
        p = request.query_params.get('p')
        p2 = request.query_params.get('p2')
        queryset = self.queryset.filter(
            Q(price__gte=p) &
            Q(price__lte=p2)
        )
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



