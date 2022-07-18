from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Task

# Create your views here.
def home(request):
    return render(request,'home.html')

def user_signup(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        print(fm)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password1']
            #print(uname)
            #print(upass)
            u=User.objects.create_user(username=uname,password=upass,is_superuser=True,is_staff=True)
            u.save()
            return HttpResponseRedirect('/u_login/')
            
    else:
        fm=UserCreationForm()
    return render(request,'user_signup.html',{'form':fm})

def u_login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        #print(fm)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            #print(uname)
            #print(upass)
            u=authenticate(username=uname,password=upass)
            if u is not None:
                #print("valid user")
                login(request,u)
                return HttpResponseRedirect('/dashboard/')
    else:
        fm=AuthenticationForm()

    return render(request,'login.html',{'form':fm})

def u_logout(request):
     logout(request)
     return HttpResponseRedirect('/')

def dashboard(request):
    #collecting authenticated user id from the session
    c=request.user
    cuid=c.id
    print(cuid)
    u=User.objects.get(id=cuid)
    print(u.is_superuser)
    b=Task.objects.all()
    content={}
    content['data']=b
    content['is_superuser']=u.is_superuser
    return render(request,'dashboard.html',content)

def new_task(request):
    if request.method=="POST":
        task_name=request.POST['task_name']
        task_detail=request.POST['task_detail']
        #print(task_name)
        # print(bauthor)
        b=Task.objects.create(name=task_name,detail=task_detail,)
        b.save()
        return HttpResponseRedirect('/dashboard')

    else:
        return render(request,'new_task.html')

def update(request,rid):
     if request.method=="POST":
        #print(rid)
        utask_name=request.POST['task_name']
        utask_detail=request.POST['task_detail']
        b=Task.objects.filter(id=rid)
        b.update(name=utask_name,detail=utask_detail)
        return HttpResponseRedirect('/dashboard/')

     else:
        b=Task.objects.filter(id=rid)
        content={}
        content['data']=b
        return render(request,'update.html',content)

def delete(request,rid):
    b=Task.objects.filter(id=rid)
    b.delete()
    return HttpResponseRedirect('/dashboard/')



