from rest_framework import serializers
from gender.models import Gender


class GenderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'