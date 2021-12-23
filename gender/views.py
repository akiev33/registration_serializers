from rest_framework import viewsets
from gender.models import Gender

from gender.serializers import GenderSerializers




class GenderAPIView(viewsets.ModelViewSet):
    serializer_class = GenderSerializers
    queryset = Gender.objects.all()