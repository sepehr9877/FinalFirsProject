from django.contrib.auth.models import User
from django.db import models
from Music.models import Music,MusicDetail
from Music.models import MusicDetail,Music
class HistoryByuser(models.Model):
    History_User=models.ForeignKey(User,on_delete=models.PROTECT)
    History_Song=models.ForeignKey(MusicDetail,on_delete=models.PROTECT)
    def __str__(self):
        return  self.History_User.username + self.History_Song.musicname.title
# Create your models here.
