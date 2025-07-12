from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer


class RoomAPIView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
