from django.db import models
class Site_Settings(models.Model):
    title=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Phone=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)

# Create your models here.
