from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import Add_comments,Subscriber_Comment,adding_comments
from .models import Subscriber,User_Comments,Comments,Blogs
def commentspage(request,*args,**kwargs):
    commentdetail=Add_comments(request.POST or None)
    subdetail=adding_comments(request.POST or None)
    blogid=kwargs["blogid"]
    if commentdetail.is_valid() and  subdetail.is_valid():
        username=subdetail.clean_username()
        email=subdetail.clean_email()
        description=commentdetail.clean_descriptions()
        selected_user=Subscriber.objects.filter(username=username,email=email)
        if selected_user:
            print("enter")
            adding_comment=Comments.objects.create(descriptions=description)
            selected_user=Subscriber.objects.filter(username=username,email=email).first()
            adding_user_comments=User_Comments.objects.create(user_comment=selected_user,comments=adding_comment,blog_comments_id=blogid)
            return redirect(f"/commentspage/{blogid}")
        else:
            return redirect(f"/addingsubscriber/{blogid}")
    selected_comments=User_Comments.objects.filter(blog_comments_id=blogid)
    selected_blog=Blogs.objects.filter(id=blogid).first()
    commentscount=User_Comments.objects.filter(blog_comments_id=blogid).values_list("comments").count()
    allblogs=Blogs.objects.all()[:3]
    context={
        "commentdetail":commentdetail,
        "subdetail":subdetail,
        "selected_comments":selected_comments,
        "selected_blog":selected_blog,
        "commentcount":commentscount,
        "Blogs":allblogs
    }
    return render(request,"commentspage.html",context)
def login_to_commentpage(request):
    subinfo=Subscriber_Comment(request.POST or None)
    if subinfo.is_valid():
        username=subinfo.clean_username()
        email=subinfo.clean_email()
        selected_user=Subscriber.objects.filter(username=username,email=email)
        if selected_user:
            return redirect("/commentspage")
        else:
            return redirect("/addingsubscriber")


def adding_subscriber(request,*args,**kwargs):
    subinfo=Subscriber_Comment(request.POST or request.FILES)
    blogid=kwargs["blogid"]
    if subinfo.is_valid():
        username=subinfo.cleaned_data.get("username")
        email=subinfo.cleaned_data.get("email")
        image_field=request.FILES['image']
        adding_sub=Subscriber.objects.create(username=username,email=email,image=image_field)
        print(adding_sub)
        return redirect(f"/commentspage/{blogid}")
    context={"subinfo":subinfo}
    return render(request,"subscriberpage.html",context)
# Create your views here.
def allblogspage(request):
    allblogs=Blogs.objects.all()
    paginator=Paginator(allblogs,6)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={"blogs":allblogs,
             "page_obj":page_obj}
    return render(request,"allblogs.html",context)