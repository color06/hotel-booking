from rest_framework import generics, filters
from .models import Room
from .serializers import RoomListSerializer, RoomDetailSerializer


class RoomAPIView(generics.ListAPIView):
    queryset = Room.objects.filter(is_published=True)
    serializer_class = RoomListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price', 'created_at']


class RoomCreateAPIView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer


class RoomUpdateAPIView(generics.UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer


class RoomDeleteAPIView(generics.DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer


class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer
