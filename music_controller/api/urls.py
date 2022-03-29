from django.urls import path
# from music_controller.api.models import Room
from .views import RoomView

urlpatterns = [
    path('home', RoomView.as_view()),
]
