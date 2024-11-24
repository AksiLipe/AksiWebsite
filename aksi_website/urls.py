from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),  # Главная страница
    path('music/', include('music.urls')),  # Приложение music
    path('users/', include('users.urls')),  # Приложение users
]