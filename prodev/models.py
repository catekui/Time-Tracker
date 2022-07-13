from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255 ,null=True, blank=True)
    image = models.ImageField(upload_to='tracker',default="Awards/avatars_kuiof2.png",blank=True)
    username = models.CharField(max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def save_user(self):
        self.save()


    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    time_interval = models.IntegerField(default=None)
    break_interval = models.IntegerField(default=None)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    efficiency = models.IntegerField()
    experience = models.IntegerField()
    productivity = models.IntegerField()
    message = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user
    
    
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"user:{self.user}, action:{self.name}"
    
class Time_Worked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action_done = models.CharField(max_length=100)
    time_worked = models.IntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"user:{self.user}, action:{self.action_done}"
    
  
   
