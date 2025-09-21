from django.db import models

# Create your models here.
class MovieModel(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} | {self.director} | {self.year}"