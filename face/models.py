from django.db import models
# Create your models here.

class app(models.Model):
    
    number = models.IntegerField()
    password = models.CharField(max_length=15)


    def __str__(self):
        return str(self.number)
