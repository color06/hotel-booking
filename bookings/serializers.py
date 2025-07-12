from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ("id", "room", "date_start", "date_end")

    def validate(self, data):
        if data["date_start"] >= data["date_end"]:
            raise serializers.ValidationError(
                "date_start должен быть меньше date_end.")

        overlaps = Booking.objects.filter(
            room=data["room"],
            date_start__lt=data["date_end"],
            date_end__gt=data["date_start"],
        )
        if self.instance:
            overlaps = overlaps.exclude(pk=self.instance.pk)

        if overlaps.exists():
            raise serializers.ValidationError(
                "Номер уже забронирован на выбранные даты.")
        return data
