from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import Student
from .models import User
# Create your views here.


def add(request):
    if request.method == 'POST':
        std=Student(request.POST)
        if std.is_valid():
            nm=std.cleaned_data['name']
            em=std.cleaned_data['email']
            pw=std.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            std=Student()
    else:
        std=Student()
    stud=User.objects.all()
    return render(request,'add.html',{'form':std,'stu':stud})


def delete(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
def update(request,id):
    if request.method == 'POST':
       pi=User.objects.get(pk=id)
       std=Student(request.POST,instance=pi)
       if std.is_valid():
           std.save()
           
       else:
           pi=User.objects.get(pk=id)
           std=Student(request.POST,instance=pi)
           return redirect("add")
           
           
    return render(request,'update.html',{'id':id})