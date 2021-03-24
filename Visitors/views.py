import datetime

from django.shortcuts import render
from django.conf import settings
from .models import Visitors_Info
import socket
import random
def save_visitors_info(request):
    try:
        x_forward_for=request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forward_for:
            ip=x_forward_for.split(',')[0]
        else:
            ip=request.META.get('REMOTE_ADDR')
        try:
            socket.inet_aton(ip)
            ip_valid=True
        except socket.error:
            ip_valid=False
        if ip_valid:
            present_date=datetime.datetime.now()
            ref_date_1=present_date.now-datetime.timedelta(days=1)
            ref_date_2=present_date.now-datetime.timedelta(days=2)

            if Visitors_Info.objects.filter(ip_address=ip,page_visited=request.path,event_date__gt=ref_date_1).count()==0:
                new_VIsitors_Info=Visitors_Info.objects.create(
                    ip_address=ip,
                    page_visited=request.path,
                    event_date=present_date,)
                new_VIsitors_Info.save()
            if Visitors_Info.objects.filter(ip_address=ip,page_visited=request.path,event_date__gt=ref_date_1).count()==1:
                visitor_infos_obj = Visitors_Info.objects.get(ip_address=ip, page_visited=request.path, event_date__gte=ref_date_1)
                visitor_infos_obj.event_date = present_date
                visitor_infos_obj.save()
    except:
        pass

    context_nb_vistors = 0
    ref_date = present_date - datetime.timedelta(minutes=5)
    context_nb_vistors = Visitors_Info.objects.filter(event_date__gte=ref_date).values_list('ip_address',
                                                                                            flat=True).distinct().count()
    context={"context_nb_vistors": context_nb_vistors}
    return render(request,"shared/footerwrapper.html",context)
# Create your views here.
