from django.db import models

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=40)

class Message(models.Model):
    room_name = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now=True)

class DummyMessage():
    def __init__(self, room_name, content, user_name, timestamp) -> None:
        self.room_name = room_name
        self.content = content
        self.user_name = user_name
        self.timestamp = timestamp
        