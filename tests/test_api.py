import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from rooms.models import Room
from bookings.models import Booking

pytestmark = pytest.mark.django_db
client = APIClient()


def create_room(**kwargs) -> Room:
    defaults = {"description": "Test room",
                "price": 1000, "is_published": True}
    defaults.update(kwargs)
    return Room.objects.create(**defaults)


def create_booking(room: Room, ds: str, de: str) -> Booking:
    return Booking.objects.create(room=room, date_start=ds, date_end=de)


def test_create_room_api():
    url = reverse("room-create")
    res = client.post(url, {"description": "Std",
                      "price": 2000, "is_published": True})
    assert res.status_code == 201
    assert Room.objects.count() == 1
    assert res.data["price"] == "2000.00"


def test_room_ordering():
    create_room(price=300)
    create_room(price=200)
    res = client.get(reverse("rooms-list") + "?ordering=price")
    prices = [int(r["price"].split(".")[0]) for r in res.data]
    assert prices == sorted(prices)


def test_booking_create_ok():
    room = create_room()
    url = reverse("booking-create")
    res = client.post(
        url,
        {"room": room.id, "date_start": "2025-01-10", "date_end": "2025-01-12"},
    )
    assert res.status_code == 201
    assert Booking.objects.count() == 1


def test_booking_overlap_rejected():
    room = create_room()
    create_booking(room, "2025-01-05", "2025-01-10")  # занята
    url = reverse("booking-create")
    res = client.post(
        url,
        {"room": room.id, "date_start": "2025-01-08", "date_end": "2025-01-12"},
    )
    assert res.status_code == 400
    assert "уже забронирован".encode() in res.content
    assert Booking.objects.count() == 1


def test_booking_delete_and_cascade():
    room = create_room()
    b = create_booking(room, "2025-02-01", "2025-02-03")
    res = client.delete(reverse("booking-delete", args=[b.id]))
    assert res.status_code == 204
    assert Booking.objects.count() == 0

    create_booking(room, "2025-03-01", "2025-03-02")
    assert Booking.objects.count() == 1
    client.delete(reverse("room-delete", args=[room.id]))
    assert Room.objects.count() == 0
    assert Booking.objects.count() == 0
