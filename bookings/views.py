from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer


class BookingCreateAPIView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDeleteAPIView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = "pk"


class BookingListAPIView(generics.ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        room_id = self.request.query_params.get("room")
        return (
            Booking.objects.filter(room_id=room_id).order_by("date_start")
            if room_id
            else Booking.objects.none()
        )
