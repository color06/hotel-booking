# Hotel-Booking API

Сервис для управления номерами отелей и их бронированиями.  
Стек — **Django 5 + Django REST Framework + PostgreSQL**.  
API без авторизации, все ответы — JSON.

---

## Быстрый старт

```bash
git clone https://github.com/color06/hotel-booking.git
cd hotel-booking
docker compose up -d

Приложение будет доступно на http://localhost:8000

Маршруты API
Endpoint	Метод	Назначение
/api/v1/roomslist/?ordering=price	GET	список опубликованных номеров (сортировка price / created_at, - — убывание)
/api/v1/rooms/create/	POST	добавить номер (description, price, is_published)
/api/v1/rooms/<id>/update/	PUT/PATCH	изменить номер
/api/v1/rooms/<id>/delete/	DELETE	удалить номер и все его брони
/api/v1/bookings/create/	POST	создать бронь (room, date_start, date_end)
/api/v1/bookings/delete/<id>/	DELETE	удалить бронь
/api/v1/bookings/list/?room=<room_id>	GET	все брони номера, отсортированы по date_start

Валидация при создании брони
date_start < date_end

нет пересечения с уже существующими бронями этой комнаты

Примеры cURL
bash
Копировать
Редактировать
# ➤ создать номер
curl -X POST http://localhost:8000/api/v1/rooms/create/ \
     -d "description=Стандарт" -d "price=3000" -d "is_published=true"

# ➤ список номеров по убыванию цены
curl "http://localhost:8000/api/v1/roomslist/?ordering=-price"

# ➤ забронировать номер id=4
curl -X POST http://localhost:8000/api/v1/bookings/create/ \
     -d "room=4" -d "date_start=2025-07-20" -d "date_end=2025-07-22"

# ➤ список броней номера 4
curl "http://localhost:8000/api/v1/bookings/list/?room=4"
Запуск тестов
bash
Копировать
Редактировать
docker compose exec web pytest
Запуск без Docker
bash
Копировать
Редактировать
poetry install
cp .env.example .env        # при необходимости
python manage.py migrate
python manage.py runserver
Принятые решения
Валидация пересечений дат реализована в BookingSerializer.

Сортировка реализована стандартным DRF OrderingFilter.

Приложения разделены по доменам: rooms и bookings.

При удалении номера каскадно удаляются все связанные брони (on_delete=models.CASCADE).