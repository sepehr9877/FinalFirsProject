from django.urls import path
from .views import CheckPurchase,purchasepage,delete_frompurchasepage,PurchaseFinished,PurchaseAlbum,TopPurchase
urlpatterns=[
    path("addtopurchase/<musicid>",CheckPurchase),
    path("addtopurchasealbum/<albumname>",PurchaseAlbum),
    path("purchase",purchasepage),
    path("deletepurchase/<musicid>",delete_frompurchasepage),
    path("PurchaseFinished",PurchaseFinished),
    path("toppurchase",TopPurchase,name="TopPurchase"),
#
]