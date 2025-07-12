from django.db import models
from rooms.models import Room


class Booking(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="bookings")
    date_start = models.DateField()
    date_end = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Бронь {self.id} для комнаты {self.room_id} с {self.date_start} по {self.date_end}"
