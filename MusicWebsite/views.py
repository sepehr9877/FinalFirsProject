import datetime
import socket

from django.shortcuts import render

from Genre.models import Genre
from Visitors.models import Visitors_Info
from comments.models import Blogs
from sitesettings.models import Site_Settings

def homepage(request):
    return render(request,"homepage.html")
def MainWrapperStart(request):
    rock = Genre.objects.filter(NameGenre__contains="Rock").first()
    hiphop = Genre.objects.filter(NameGenre__contains="HipHop").first()
    classic = Genre.objects.filter(NameGenre__contains="Classic").first()
    love = Genre.objects.filter(NameGenre__contains="Love").first()
    print(love)
    EDm = Genre.objects.filter(NameGenre__contains="EDM").first()
    Happy = Genre.objects.filter(NameGenre__contains="Happy").first()
    print(Happy)
    Blooz = Genre.objects.filter(NameGenre__contains="Bloze").first()
    Cell = Genre.objects.filter(NameGenre__contains="sell").first()
    Single = Genre.objects.filter(NameGenre__contains="Single").first()
    metal = Genre.objects.filter(NameGenre__contains="Metal").first()
    Jazz = Genre.objects.filter(NameGenre__contains="Jazz").first()
    pop = Genre.objects.filter(NameGenre__contains="Pop").first()
    folk = Genre.objects.filter(NameGenre__contains="Folk").first()
    context = {
        "rock": rock,
        "hiphop": hiphop,
        "classic": classic,
        "love": love,
        "EDM": EDm,
        "Happy": Happy,
        "Bloze": Blooz,
        "Cell": Cell,
        "Single": Single,
        "metal": metal,
        "jazz": Jazz,
        "pop": pop,
        "folk": folk
    }
    return render(request,"shared/MainWrapperStart.html",context)
def footerwrapper(request):
    sitesetting=Site_Settings.objects.all().first()
    try:
        x_forward_for=request.META.get('HTTP_X_FORWARDED_FOR')
        print(x_forward_for)
        if x_forward_for:
            ip=x_forward_for.split(',')[0]
            print(ip)
        else:
            ip=request.META.get('REMOTE_ADDR')
            print(ip)
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
    blogid=Blogs.objects.all().first()
    context={"sitesettings":sitesetting,
             # "context_nb_vistors": context_nb_vistors,
             "blog":blogid}
    return render(request,"shared/footerwrapper.html",context)