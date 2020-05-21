from django.db import models

# Create your models here.
class Jsondb(models.Model):
    number=models.IntegerField(auto_created=0)
    name=models.CharField(max_length=50)
    version=models.IntegerField(default=0)
    json=models.CharField(max_length=500)
    def __str__(self):
        return self.name