from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Image(models.Model):
    image=models.ImageField(upload_to='images/')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Done'
    
class Password(models.Model):
    Username=models.CharField(max_length=30)
    Password=models.CharField(max_length=128)

    def save(self,*args,**kwargs):
        self.Password=make_password(self.Password)
        super().save(*args,**kwargs)
