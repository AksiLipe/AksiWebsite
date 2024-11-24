from django.urls import path
from . import views

urlpatterns = [
    path('tracks/', views.track_list, name='track_list'),  # Список треков
    path('beats/', views.beat_list, name='beat_list'),  # Список битов
]