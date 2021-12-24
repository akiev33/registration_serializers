from rest_framework import serializers
from .models import Basket


class BasketSerializers(serializers.ModelSerializer):
    count = serializers.IntegerField(required=True)
    total = serializers.IntegerField(read_only=True)
    class Meta:
        model = Basket
        fields = ('count', 'product_id', 'total')

