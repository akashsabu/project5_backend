from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    age = models.IntegerField()   

    class Meta:
        db_table = "user_profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return str(self.name)   
