from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Category(models.Model):
    cat_name = models.TextField(max_length=50)
    def __str__(self):
        return self.cat_name

class Usersignup(models.Model):
    username = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    Contactno = models.CharField(max_length=12)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.name        
    
class Post(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    username = models.ForeignKey(Usersignup , on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="blog/images",default="")
    date =  models.DateTimeField()  
    def __str__(self):
        return self.title  
    

class Comment(models.Model):
    name = models.CharField(max_length=20)
    query = models.TextField()
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=11)
    email_id = models.EmailField(max_length=50)
    query =  models.TextField()  
    def __str__(self):
        return self.name,self.contact_no,self.email_id

class Subscription(models.Model):
    email_id = models.EmailField(max_length=50)
    def __str__(self):
        return self.email_id  

class Userlogin(models.Model):
    username = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username


        