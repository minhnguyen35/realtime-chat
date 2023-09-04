from django.db import models

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    salt = models.CharField(max_length=200)
    email = models.CharField(max_length=100, primary_key=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["user_name"], name="user_name"),
            models.Index(fields=["email"], name="email")
        ]