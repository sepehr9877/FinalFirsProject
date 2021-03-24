from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .form import LoginForm,Registerform,Image_user_Form
from django.contrib.auth import logout as auth_logout
from contact.models import Followers
from .models import UserProfile
equal_follow=False
accept=False
def newregisterinpage(request):
    if request.user.is_authenticated:
        return redirect("/")
    newform=Registerform(request.POST or request.FILES)
    image_user_detail=Image_user_Form(request.POST or request.FILES)
    if newform.is_valid() and (image_user_detail.is_valid() is False):
        imageuser=request.FILES['image_user']
        print(imageuser)
        username = newform.clean_username()
        print(username)
        email = newform.cleaned_data.get("email")
        send_mail("WellCome to My WebSite","Hello dear User",settings.EMAIL_HOST_USER,[email],fail_silently=False)
        password = newform.cleaned_data.get("password")
        repassword=newform.clean_repassword()
        print(repassword)
        newuser = User.objects._create_user(username=username, email=email, password=password, is_staff=True)
        createprofile=UserProfile.objects.create(user_sub_id=newuser.id,image_user=imageuser)
        user = authenticate(request, username=username, password=repassword)
        if user is not None:
            login(request, user)
        return redirect("/")

    context = {"registerform": newform,
               "image_user_form":image_user_detail}
    return render(request, "accountpage/Register.html", context)

def newloginpage(request):
    loginform = LoginForm(request.POST or None)
    if loginform.is_valid():
        username = loginform.clean_username()
        password = loginform.cleaned_data.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            send_mail("You are Login","SomeOne login to website by your account",settings.EMAIL_HOST_USER,['sepehrseifpour9877@gmail.com'],fail_silently=False)
            return redirect("/")
    context = {"loginform": loginform}
    return render(request, "accountpage/newloginpage.html",context)
@login_required(login_url="/login")
def profiledetail(request):
    userid=request.user.id
    userdetail=User.objects.filter(id=userid).values_list("username")
    print(userdetail)
    context={"userdetail":userdetail[0][0]}
    return render(request,"accountpage/profileDetail.html",context)
def logoutdetail(request):
    auth_logout(request)
    return redirect("/")
def MyRequests(request):
    userid=request.user.id
    user_requests=Followers.objects.filter(to_user_id=userid,accept_by_user=False).values_list("from_user_id")
    print("ddbd")
    print(user_requests)
    if user_requests:
        from_user_id=[]
        for i in user_requests:
            from_user_id.append(i[0])
        User_request_profile=[]
        for i in from_user_id:
            User_request_profile.extend(UserProfile.objects.filter(user_sub_id=i))
        context={"userrequests":User_request_profile}
        return render(request,"accountpage/MyFriends.html",context)
    else:
        context={}
        return render(request, "accountpage/MyFriends.html", context)
def accept_my_request(request,*args,**kwargs):
    user_to_id=request.user.id
    from_user=kwargs["from_user"]
    accept_request=Followers.objects.filter(to_user_id=user_to_id,from_user_id=from_user).update(accept_by_user=True)
    return redirect("/MyFreindsPage")
def restric_my_follwers(request,*args,**kwargs):
    user_to_id = request.user.id
    user_from=kwargs["from_user"]
    accept_request = Followers.objects.filter(to_user=user_to_id, from_user_id=user_from).update( accept_by_user=False)
    return redirect("/MyFreindsPage")
def MyFollowers(request):
    to_user=request.user.id
    select_user_from=Followers.objects.filter(to_user_id=to_user,accept_by_user=True).values_list("from_user_id")
    list_followers=[]
    for i in select_user_from:
        list_followers.extend(UserProfile.objects.filter(user_sub_id=i[0]))
    global equal_follow
    accept_by=Followers.objects.filter(from_user_id=to_user,accept_by_user=False)
    print("scc")
    print(accept_by)
    if accept_by:
        accept=False
    else:
        accept=True
    context={"myfollowers":list_followers,
             "equal":equal_follow}
    return render(request,"accountpage/MyFollower.html",context)
def Follow_the_user(request,*args,**kwargs):
    from_user=kwargs["from_user"]
    to_user=request.user.id
    follow_the_user=Followers.objects.create(from_user_id=to_user,to_user_id=from_user,accept_by_user=False)
    return redirect("/MyFreindsPage")
def MyWaitings(request):
    from_user=request.user.id
    selected_users=Followers.objects.filter(from_user_id=from_user,accept_by_user=False).values_list("to_user_id")
    to_user_select=[]
    if selected_users:
        for i in selected_users:
            to_user_select.extend(UserProfile.objects.filter(user_sub_id=i[0]))
        context={"selected_users":to_user_select}
        return render(request,"accountpage/Waintings.html",context)
    else:
        return render(request, "accountpage/Waintings.html")
def MyFollowing(request):
    to_user=request.user.id
    select_user=Followers.objects.filter(from_user_id=to_user,accept_by_user=True).values_list("to_user_id")
    print("myyy")
    print(select_user)
    if select_user:
        followings=[]
        for i in select_user:
            print(i)
            followings.extend(UserProfile.objects.filter(user_sub_id=i[0]))
        print(followings)
        context={"Followings":followings}
        return render(request,"accountpage/MyFollowing.html",context)
    else:
        return render(request,"accountpage/MyFollowing.html")
def deny_request(request,*args,**kwargs):
    to_user=kwargs["to_user"]
    from_user=request.user.id
    deny__request=Followers.objects.filter(to_user_id=to_user,from_user_id=from_user).delete()
    return redirect("/MyFreindsPage")
def UnFollowUsers(request,*args,**kwargs):
    to_user=kwargs["to_user"]
    from_user=request.user.id
    UnFollow=Followers.objects.filter(to_user_id=to_user,from_user_id=from_user,accept_by_user=True).delete()
    return redirect("/MyFreindsPage")
def MyFriendsPage(request):
    return render(request,"accountpage/MyFriendsPage.html")