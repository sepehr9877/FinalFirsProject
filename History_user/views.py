from django.shortcuts import render, redirect
from .models import  HistoryByuser
def HistoryPage(request):
    userid=request.user.id
    all_history=HistoryByuser.objects.filter(History_User_id=userid)
    if len(all_history)>50:
        HistoryByuser.objects.filter(History_User_id=userid).delete()
    context={"all_history":all_history}
    return render(request,"HistoryPage.html",context)
def DeleteHistory(request):
    userid=request.user.id
    deleted_history=HistoryByuser.objects.filter(History_User_id=userid).delete()
    return redirect("/History")
# Create your views here.
