from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="receiver"
    )
    message = models.CharField(max_length=800)
    subject = models.CharField(max_length=200)
    creation_date = models.DateTimeField("date published", auto_now_add=True)
    unread = models.BooleanField(default=True)

    def __str__(self):
        return (
            "from: "
            + self.sender
            + ", to: "
            + self.receiver
            + ".\n message: "
            + self.message
        )