from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)
    is_logged = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username