from django.urls import path
from .views import (
    BookingListAPIView,
    BookingCreateAPIView,
    BookingDetailAPIView,  # <‑‑ GET one
    BookingDeleteAPIView,
)

urlpatterns = [
    # GET /api/v1/bookings/?room=<id>
    path("", BookingListAPIView.as_view(), name="booking-list"),
    # POST /api/v1/bookings/
    path("create/", BookingCreateAPIView.as_view(), name="booking-create"),
    # GET /api/v1/bookings/<pk>/
    path("<int:pk>/", BookingDetailAPIView.as_view(), name="booking-detail"),
    # DELETE /api/v1/bookings/<pk>/delete/
    path("<int:pk>/delete/", BookingDeleteAPIView.as_view(), name="booking-delete"),
]
