from django.db import models
class Visitors_Info(models.Model):
    ip_address=models.GenericIPAddressField()
    page_visited=models.TextField()
    event_date=models.DateTimeField()
# Create your models here.
