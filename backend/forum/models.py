from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser) :
    roleChoices = (
        ('B', 'Base'),
        ('M', 'Mod'),
        ('A', 'Admin')
    )
    credit = models.IntegerField(default=0)
    role = models.CharField(max_length=1, choices=roleChoices, default='B')
    
    def __str__(self) :
        return self.username

# Create your models here.
class Question(models.Model) :
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    img =  models.ImageField(upload_to='qpics/', blank=True)
    upvoted = models.IntegerField(default=0)
    
    def __str__(self) :
        return self.title + '\n' + self.content

class Answer(models.Model) :
    answer_to = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    img = models.ImageField(upload_to='apics/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upvoted = models.BooleanField(default=False)

    def __str__(self) :
        return self.content
    


