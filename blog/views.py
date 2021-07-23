from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from .models import matlabs
from .forms import matlabform
from django.urls import reverse
from django.db.models import Q

def home(request):
    writer, created = Group.objects.get_or_create(name='writer')
    return render(request,"base.html")

def signup(request):
    error_pass = False
    error_user = False
    error_null = False
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        password_repeat = request.POST.get("password2")

        if username=='' or email=='' or password=='' or password_repeat=='' :
            error_null = True
            return render(request, "signup.html",{"error_null":error_null})

        if password != password_repeat :
            error_pass = True
            return render(request, "signup.html", {"error_pass": error_pass})

        if User.objects.filter(username=username).exists() :
            error_user = True
            return render(request, "signup.html", {"error_user": error_user})

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password)
        user.save()

        return HttpResponseRedirect("/")
    return render(request, "signup.html")

def log_in(request):
    error_login = False
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        elif user is None:
            error_login = True
    return render(request, "login.html", {
        "error_login": error_login
    })

def log_out(request):
    logout(request)
    return HttpResponseRedirect("/")

def contact(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        text = request.POST.get("text")
        email = request.POST.get("email")
        send_mail(
                title,
                f"{text}  {email}",
                'email@a.com',
                ["email2@a.com"],
            )
        return render(request, "contact-success.html")
    return render(request, "contact.html")

def panel(request):
    writer, created = Group.objects.get_or_create(name='writer')
    flagg = False
    if request.method == 'POST':
        writer.user_set.add(request.user)
        return render(request, "writer-done.html",{"flagg": flagg})
    if request.user.groups.filter(name = 'writer').exists():
        flagg = True
    else:
        flagg = False
    print(flagg)
    return render(request, "panel.html",{"flagg": flagg})

def addmatlab(request):
    writer, created = Group.objects.get_or_create(name='writer')
    flagg = False
    if request.user.groups.filter(name = 'writer').exists():
        flagg = True
        print(flagg)
    else:
        flagg = False
        print(flagg)
    if request.method == 'POST':
        title = request.POST.get("title")
        mohtava = request.POST.get("mohtava")
        matlab = matlabs(title=title,mohtava=mohtava,author=request.user)
        matlab.save()
        return render(request, "matlab-success.html")
    return render(request, "addmatlab.html",{"flagg": flagg})
  
def matlablistuser(request):
    user_matlabs = matlabs.objects.filter(author=request.user)
    return render(request, "usermatlabs.html",{"user_matlabs":user_matlabs})

def searchmatlabs(request):
    error_search = False
    searchmatlabs = matlabs.objects.all()
    if request.method == "POST":
        query = request.POST.get("title")
        search_list = matlabs.objects.filter(title__contains=query)
        if not search_list.all().exists() :
            error_search = True
            print(1)
            return render(request, "matlabs.html", {"error_search": error_search})
        else:
            return render(request, "search.html", {"search_list": search_list })
    return render(request, "matlabs.html",{"searchmatlabs":searchmatlabs})

def editmatlab(request , id=None):
    post = get_object_or_404(matlabs, id=id)
    editform = matlabform(request.POST or None , request.FILES or None, instance=post)
    if editform.is_valid():
        editform.save()
        return HttpResponseRedirect('/mymatlabs')
    context = {
        'form': editform,
    }
    return render(request, 'editmatlab.html',context)

def deletematlab(request , id=None):
    post = get_object_or_404(matlabs, id=id)
    if post.delete():
        return HttpResponseRedirect('/mymatlabs')

def homematlab(request):
    postha = matlabs.objects.all()
    context = {
        'postha' : postha
    }
    print(postha.all())
    return render(request, 'base.html',context)

def detail(request , id=None):
    post = get_object_or_404(matlabs, id=id)
    context = {
        'post' : post
    }
    return render(request, 'detail.html' , context)