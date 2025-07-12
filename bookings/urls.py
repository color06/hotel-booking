from django.urls import path
from .views import BookingCreateAPIView, BookingDeleteAPIView, BookingListAPIView

urlpatterns = [
    path("create/", BookingCreateAPIView.as_view(), name="booking-create"),
    path("delete/<int:id>/", BookingDeleteAPIView.as_view(), name="booking-delete"),
    path("list/", BookingListAPIView.as_view(), name="booking-list"),
]
