from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.TextField(max_length=50)
    age=models.IntegerField()
    gender=models.TextField(max_length=6)
    image = models.ImageField(upload_to="blog/images",default="")
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Persons"