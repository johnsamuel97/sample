from django.db import models


# Create your models here.
class Record(models.Model):
    name=models.CharField(max_length=60)
    mobile_no=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=90)
    

    
