from rest_framework import viewsets
from personal.permission import IsOwnerOrReadOnly
from personal.serializers import PersonalSerializers
from rest_framework.response import Response




class PersonalAPIView(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PersonalSerializers

    def list(self, request, *args, **kwargs):
        first_name = request.user.first_name
        last_name = request.user.last_name
        age = request.user.age
        gender = request.user.gender_type
        return Response({"first_name": first_name, "last_name": last_name, "age": age, "gender": gender})


    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()