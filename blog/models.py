from django.db import models

class Able(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name