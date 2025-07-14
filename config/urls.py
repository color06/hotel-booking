from django.contrib import admin
from django.urls import path, include

from rooms.views import (
    RoomAPIView,
    RoomCreateAPIView,
    RoomDetailAPIView,
    RoomUpdateAPIView,
    RoomDeleteAPIView,
)
from bookings.views import BookingCreateAPIView, BookingDeleteAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/roomslist/", RoomAPIView.as_view(), name="rooms-list"),
    path("api/v1/rooms/create/", RoomCreateAPIView.as_view(), name="room-create"),
    path("api/v1/rooms/<int:pk>/", RoomDetailAPIView.as_view(), name="room-detail"),
    path(
        "api/v1/rooms/<int:pk>/update/", RoomUpdateAPIView.as_view(), name="room-update"
    ),
    path(
        "api/v1/rooms/<int:pk>/delete/", RoomDeleteAPIView.as_view(), name="room-delete"
    ),
    path(
        "api/v1/bookings/create/", BookingCreateAPIView.as_view(), name="booking-create"
    ),
    path(
        "api/v1/bookings/delete/<int:pk>/",
        BookingDeleteAPIView.as_view(),
        name="booking-delete",
    ),
    path("api/v1/bookings/", include("bookings.urls")),
]
