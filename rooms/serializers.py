from rest_framework import serializers
from .models import Room


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        read_only_fields = ("id", "created_at", "update_at")


class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("id", "description", "price", "is_published")
