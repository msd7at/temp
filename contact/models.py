from django.db import models

# Create your models here.
class info (models.Model):
    iname=models.CharField(max_length=35)
    iage=models.IntegerField()
    iemail=models.CharField(max_length=35)
    imsg=models.CharField(max_length=1000)
    def __str__(self):
        return self.iname
