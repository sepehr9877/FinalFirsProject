import datetime

from django.contrib.auth.models import User
from django.db import models
from Music.models import MusicDetail, Music


class PurchaseManage(models.Manager):
   def checkid(self,userid):
       user=PurchaseUser.objects.filter(user_purchase_id=userid).first()
       print("user purchase")
       print(user)
       if not user:
           print("enter to")
           user=PurchaseUser.objects.create(user_purchase_id=userid,date=datetime.datetime.now(),is_paid=False)
           return user
       return user
   def checkmusicid(self,userid,musicid):
       user_purchase_music=PurchaseUserMusic.objects.filter(Purchase_User_id=userid,Music_Purchase_id=musicid).first()
       print("user___")
       print(user_purchase_music)
       user=PurchaseUser.objects.filter(user_purchase_id=userid)
       if not user_purchase_music:
           user_purchase_music=PurchaseUserMusic.objects.create(Purchase_User_id=user.id,Music_Purchase_id=musicid)
           return user_purchase_music
       return user_purchase_music
   def get_common_purchase(self):
       userpurchase=PurchaseUser.objects.all().values_list("user_purchase_id")
       users_id=[]
       for i in userpurchase:
           users_id.append(i[0])

       useronepurchase=PurchaseUserMusic.objects.filter(Purchase_User__user_purchase_id=users_id[0],is_paid_music=True).values_list("Music_Purchase_id")
       print(useronepurchase)
       songone=[]
       for i in useronepurchase:
           songone.append(i)
       print("songone")
       print(songone)
       selected_song=[]
       help_song=[]
       start_song_user=[]
       for i in range(1,len(users_id)):
           print("enter")
           start_song_user.extend(PurchaseUserMusic.objects.filter(Purchase_User__user_purchase_id=users_id[i],is_paid_music=True).values_list("Music_Purchase_id"))
           print("start_song_user")
           print(start_song_user)
           if not selected_song:
               for j in start_song_user:
                   for s in songone:
                       if j == s:
                           selected_song.append(j)
               start_song_user=[]
           else:
               for s in selected_song:
                   for h in start_song_user:
                       if h==s:
                           help_song.append(h)
               selected_song=[]
               for h in help_song:
                   selected_song.append(h)
               help_song=[]
       selectsong=[]
       for s in selected_song:
           selectsong.extend(Music.objects.filter(id=s[0]))
       print(selectsong)
       selectsong=list(dict.fromkeys(selectsong))
       return selectsong
class PurchaseUser(models.Model):
    user_purchase=models.ForeignKey(User,on_delete=models.PROTECT)
    date=models.DateTimeField(default=datetime.datetime.now())
    is_paid=models.BooleanField(default=False)
    def __str__(self):
        return self.user_purchase.username





class PurchaseUserMusic(models.Model):
    Purchase_User=models.ForeignKey(PurchaseUser,on_delete=models.CASCADE)
    Music_Purchase=models.ForeignKey('Music.Music',on_delete=models.PROTECT)
    is_paid_music=models.BooleanField(default=False)
    objects=PurchaseManage()
    def __str__(self):
        return self.Music_Purchase.title

# Create your models here.
