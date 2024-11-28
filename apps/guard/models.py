from django.db import models

class Guarder(models.Model):
    full_name = models.CharField(max_length=200)
    job = models.CharField(max_length=100)
    image = models.ImageField(upload_to='guarder-img/')

    def __str__(self):
        return self.full_name
