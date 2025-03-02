from django.db import models

class customers(models.Model):
    name=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    phone=models.IntegerField()
    image=models.ImageField(upload_to='uploads/')
    resume=models.ImageField(upload_to='uploads/')
