from django.contrib import admin
from django.urls import path
from gallery.views import welcome, index, admin_dashboard
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('django-admin/', admin.site.urls), # Системный вход
    path('', welcome, name='welcome'),       # Теперь самый первый адрес открывает Выбор Роли!
    path('catalog/', index, name='index'),   # Каталог переехал на /catalog/
    path('panel/', admin_dashboard, name='admin_dashboard'), # Наша CRM-панель
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
