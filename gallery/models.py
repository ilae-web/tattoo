from django.db import models
from django.contrib.auth.models import User


# Первая таблица (для готовых эскизов админа)
class ArtPiece(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название картины")
    image = models.ImageField(upload_to='gallery_images/', verbose_name="Изображение")
    style = models.CharField(max_length=100, verbose_name="Стиль")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена (руб.)")
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Кто загрузил")
    is_approved = models.BooleanField(default=False, verbose_name="Одобрено админом")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.style}) — {self.price} руб."


# Вторая таблица (для онлайн-записи клиентов)
class Appointment(models.Model):
    client_name = models.CharField(max_length=100, verbose_name="Имя клиента")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    date = models.DateField(verbose_name="Дата сеанса")
    time = models.TimeField(verbose_name="Время сеанса")

    custom_image = models.ImageField(upload_to='custom_designs/', blank=True, null=True,
                                     verbose_name="Свой эскиз пользователя")
    custom_style = models.CharField(max_length=100, blank=True, null=True, verbose_name="Свой стиль")
    custom_size = models.CharField(max_length=50, blank=True, null=True, verbose_name="Размер (например, 15х10 см)")

    comment = models.TextField(blank=True, verbose_name="Комментарий или выбранный готовый эскиз")

    # Вот ОНА — наша новая строчка статуса!
    status = models.CharField(max_length=20, default='На проверке', verbose_name="Статус")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Запись: {self.client_name} — {self.date} ({self.status})"
