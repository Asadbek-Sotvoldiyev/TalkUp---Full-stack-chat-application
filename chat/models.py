from django.db import models
from users.models import User


class ChatGroup(models.Model):
    name = models.CharField(max_length=250)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
    

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    chatgroup = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to="files/", null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
    
