from django.urls import path
# from music_controller.api.models import Room
from .views import RoomView, CreateRoomView

urlpatterns = [
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view())

]
