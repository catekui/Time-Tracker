from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cloudinary')
    
class Project(models.Model):

    user = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    # user = models.ForeignKey(User)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.CharField(max_length=255)
    time_interval = models.IntegerField(default=None)
    break_interval = models.IntegerField(default=None)
    activity = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    
class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    efficiency = models.IntegerField()
    experience = models.IntegerField()
    productivity = models.IntegerField()





    

