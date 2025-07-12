from django.contrib import admin
from django.urls import path, include

from rooms.views import (
    RoomAPIView,
    RoomCreateAPIView,
    RoomUpdateAPIView,
    RoomDeleteAPIView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/v1/roomslist/",               RoomAPIView.as_view()),
    path("api/v1/rooms/create/",            RoomCreateAPIView.as_view()),
    path("api/v1/rooms/<int:pk>/update/",   RoomUpdateAPIView.as_view()),
    path("api/v1/rooms/<int:pk>/delete/",   RoomDeleteAPIView.as_view()),

    path("api/v1/bookings/", include("bookings.urls")),
]
