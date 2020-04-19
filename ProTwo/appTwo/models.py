from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264)
    second_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=254,unique=True)

    # def __str__(self):
    #     return self.first_name
