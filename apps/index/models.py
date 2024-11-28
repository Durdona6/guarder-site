from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField()
    description = models.TextField()

class Home(models.Model):
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.email
