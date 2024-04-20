from django.db import models
from forum.models import CustomUser

# Create your models here.

class Server(models.Model) :
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="spics/", default="spics/fallback.png", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(CustomUser)

class Channel(models.Model) :
    name = models.CharField(max_length=50)
    inServer = models.ForeignKey(Server, related_name="channels", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model) :
    content = models.TextField(max_length = 1000)
    inChannel = models.ForeignKey(Channel, related_name="messages", on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="mpics/", blank=True)
