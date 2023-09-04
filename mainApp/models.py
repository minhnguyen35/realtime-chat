from django.db import models
from authentication.models import Users
# Create your models here.
class Conversations(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=["name"], name="conversation_name")
        ]
class User_Conversations(models.Model):
    user_email = models.ForeignKey(Users, on_delete=models.CASCADE)
    conversation_id = models.ForeignKey(Conversations, on_delete=models.CASCADE)
class Messages(models.Model):
    conversation_id = models.ForeignKey(Conversations, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=["content"], name="content")
        ]

class DummyMessage():
    def __init__(self, room_name, content, user_name, timestamp) -> None:
        self.room_name = room_name
        self.content = content
        self.user_name = user_name
        self.timestamp = timestamp
        