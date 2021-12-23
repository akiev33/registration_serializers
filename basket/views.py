from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Basket
from products.models import Product
from .serializers import BasketSerializers


class BasketAPIView(APIView):

    def post(self, request):
        user = self.request.user
        count = self.request.data['count']
        product_id = self.request.data['product_id']
        product = Product.objects.filter(id=product_id).first()
        total = product.price * count
        product.quantity -= count
        product.save()
        basket = Basket.objects.create(total=total, product_id=product, user_id=user, count=count)
        serilizer = BasketSerializers(basket)
        return Response(serilizer.data)



