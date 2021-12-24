from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Basket
from products.models import Product
from .serializers import BasketSerializers
from rest_framework import generics



class BasketAPIView(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializers

    def perform_create(self, serializer):
        user = self.request.user
        count = self.request.data.get('count')
        product_id = self.request.data.get('product_id')
        product = Product.objects.filter(id=product_id).first()
        total = product.price * count
        product.quantity -= count
        product.save()
        basket = Basket.objects.create(total=total, product_id=product, user_id=user, count=count)
        serilizer = BasketSerializers(basket)
        return Response(serilizer.data)


class BasketDeleteAPIView(generics.DestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializers
    lookup_field = 'id'

    def get_queryset(self):
        queryset = Basket.objects.filter(user_id=self.request.user)
        return queryset