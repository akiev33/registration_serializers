from rest_framework import serializers
from .models import Basket


class BasketSerializers(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('__all__')
        extra_kwargs = {'product_id': {'required': True},
                        'count': {'required': True}
                        }

