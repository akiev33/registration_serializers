from rest_framework import serializers

from personal.models import Personal


class PersonalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'