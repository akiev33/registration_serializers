from rest_framework import serializers

from .models import Favorite


class FavoriteCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

    def create(self, validated_data):
        product = validated_data.get('product_id')
        user = self.context.get('user')
        favorite = Favorite.objects.create(product_id=product, user_id=user)

        return favorite

    
