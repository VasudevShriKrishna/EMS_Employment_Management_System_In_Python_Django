from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse

from empapp.models import leave
from .models import Emp,attendance
from django.db.models import Q
import datetime


def emp_home(request):
    emps=Emp.objects.all().order_by('name')
    return render(request,"emp/home.html",{'emps':emps})


def add_emp(request):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")
        emp_password=request.POST.get("emp_password")
        new_user = User.objects.create_user(
            username=emp_name,

            password=emp_password,

            )
        new_user.save()
        e=Emp()
        e.user=new_user
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        e.password=emp_password
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    # print("Yes Bhai")
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })

def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")
        # emp_password=request.POST.get("emp_department")

        e=Emp.objects.get(pk=emp_id)

        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
    return redirect("/emp/home/")
def search(request):
    text=request.GET.get('search')
    print(text)
    multiple_q = Q(Q(name__icontains=text) | Q(department__icontains=text))
    emps=Emp.objects.filter(multiple_q)
    return render(request,'emp/home.html',{'emps':emps})


def Login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        account = authenticate(username=username, password=password)
        print(account)
        if account is not None:
            print(True)
            u1 = authenticate(username=username, password=password).is_superuser
            print('u1', u1)
            if u1 == True:
                login(request, account)
                return redirect('/emp/home/')

            else:
                login(request, account)
                # messages.warning(request, "You do not have to access for login ")
                return redirect('/empapp/home/')

        else:
            messages.warning(request, "E-mail or Password Incorrect!!!")
            return render(request, 'emp/login.html',)
    else:
        pass
    return render(request, 'emp/login.html')

def leavelist(request):
    l=leave.objects.all()
    for i in l:
        print(i.status)
    return render(request,'emp/leavelist.html',{'l':l})

def leaveapprove(request,id):
    li=leave.objects.get(id=id)
    print(li)

    li.status='1'
    li.save()
    return redirect('/emp/leavelist/')

def leavereject(request,id):
    l=leave.objects.get(id=id)
    print(l)
    l.status='2'
    l.save()
    return redirect('/emp/leavelist/')

def attendancedetail(request):
    at=attendance.objects.all().order_by('-date')
    for i in at:
        print(i.totalhours())


    return render(request,'emp/attendancedetail.html',{'at':at})

def viewprofile(request,emp_id):
    emp = Emp.objects.get(pk=emp_id)
    return render(request,'emp/profile.html',{'emp':emp})


def Logout(request):
    logout(request)
    return redirect('/')
