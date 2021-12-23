from rest_framework import viewsets
from personal.permission import IsOwnerOrReadOnly
from personal.serializers import PersonalSerializers
from personal.models import Personal




class PersonalAPIView(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PersonalSerializers
    queryset = Personal.objects.all()

    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()