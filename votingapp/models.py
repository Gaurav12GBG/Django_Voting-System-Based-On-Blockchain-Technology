from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    Issue = models.TextField(max_length=250, null=True)

    def __str__(self):
        return self.email
    
class VerificationDetails(models.Model):
    sno = models.AutoField(primary_key=True)
    adharno = models.CharField(max_length=255)
    voterid = models.CharField(max_length=255)
    
    def __str__(self):
        return self.adharno
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forgot_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username