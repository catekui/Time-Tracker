from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cloudinary')
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    choices_activity = (
        ('meditation','Maditation'),
        ('stretch','Stretch'),
        ('run','Run'),
        ('take a walk','Take a walk'),
        ('listen to music','Listen to music'),
        ('take a glass of water','Take a glass of water'),
        
        
    ) 
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    time_interval = models.IntegerField(default=None)
    break_interval = models.IntegerField(default=None)
    activity = models.CharField(max_length=255,choices= choices_activity)
    date_added = models.DateTimeField(auto_now_add=True)
    
class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    efficiency = models.IntegerField()
    experience = models.IntegerField()
    productivity = models.IntegerField()




    

