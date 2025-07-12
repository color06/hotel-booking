from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer


class BookingCreateAPIView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDeleteAPIView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = "id"


class BookingListAPIView(generics.ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        room_id = self.request.query_params.get("room")
        qs = Booking.objects.all().order_by("date_start")
        return qs.filter(room_id=room_id) if room_id else qs.none()
