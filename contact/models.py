from django.contrib.auth.models import User
from django.db import models
from account.models import UserProfile
class Followers(models.Model):
    from_user=models.ForeignKey(User,on_delete=models.PROTECT,related_name="FromUser")
    to_user=models.ForeignKey(User,on_delete=models.PROTECT,related_name="ToUSer")
    accept_by_user=models.BooleanField(default=False)
    def __str__(self):
        return self.from_user.username +"follow" +self.to_user.username
# Create your models here.
