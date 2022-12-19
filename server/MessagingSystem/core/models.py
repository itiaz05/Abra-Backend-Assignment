from django.db import models

# Create your models here.

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(max_length=200, on_delete=models.CASCADE, related_name='sender', to='user')
    receiver = models.ForeignKey(max_length=200, on_delete=models.CASCADE, related_name='receiver', to='User')
    message = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date published', auto_now_add=True)
    
    def __str__(self):
        return "from: " + self.sender +  ", to: " + self.receiver + ". message: " + self.message