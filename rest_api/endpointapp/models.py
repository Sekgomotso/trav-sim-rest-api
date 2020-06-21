from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.name