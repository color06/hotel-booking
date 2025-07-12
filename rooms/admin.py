from django.contrib import admin
from .models import Room

admin.site.site_header = "Панель администрации:"
admin.site.index_title = "Сервис бронирования номеров:"


admin.site.register(Room)
