from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from emp.models import Emp, attendance
# import datetime
# import time
from datetime import datetime

from myapp.settings import MEDIA_URL,MEDIA_ROOT
from .models import leave
# Create your views here.

# def clockin(request):
#
#     if request.method == 'POST':
#         user = request.user.emp.id
#         print(user)
#         #
#         t = request.POST['clockin']
#         print(t, '''tttt''')
#         # if t == 'True':
#             #     print(True,'ttttttt')
#             #     t = request.POST['timein']
#         current_time = datetime.now().time()
#         current_date = datetime.now().date()
#         print(current_date)
#         print(current_time)
#         a = attendance(emp_id=user, timein=current_time, timeout='00:00', date=current_date)
#         a.save()
#         print('a', a)
#         return render(request, 'empapp/home.html',{'t':t})
#     else:
#         pass
#     return render(request,'empapp/home.html')
#
#
#
# def clockout(request):
#     if request.method == 'POST':
#         user = request.user.emp.id
#         print(user)
#
#         t = request.POST['clockout']
#         current_date = datetime.now().date()
#         print(current_date)
#         print('sds', True)
#         time_out = datetime.now().time()
#         a = attendance.objects.filter(emp_id=user, date=current_date).update(timeout=time_out)
#         print('time_out', time_out)
#         return render(request, 'empapp/home.html', {'time_out': time_out})
#         # a.timeout=time_out
#
#         # current_time = datetime.now().strftime('%H:%M:%S')
#
#         # print(time.asctime(time.localtime(time.time())))
#         # return redirect('/')
#
#     return render(request, 'empapp/home.html')
#
def clockin(request):
     user=request.user.emp.id
     print(user,'uuuuu')
     current_time = datetime.now().time()
     current_date = datetime.now().date()
     print(current_date)
     print(current_time)
     if attendance.objects.filter(emp=user, clock=2, date=current_date):
         print(True)
         messages.warning(request," you are already clocked in ")
         return redirect('/empapp/home/')

         # return render(request,'empapp/home.html/')
         # return HttpResponse('you already clock in ')

     else:

         clock = 1
         a = attendance(emp_id=user, timein=current_time, timeout='00:00', date=current_date, clock=clock)
         a.save()


     return redirect('/empapp/home/')

def clockout(request):
    user = request.user.emp.id
    print(user,'user')
    current_date = datetime.now().date()
    print(current_date)
    print('sds', True)
    time_out = datetime.now().time()
    if attendance.objects.filter(emp=user,clock=1,date=current_date).update(clock=2,timeout=time_out):
        print(True)

    # a.timeout = time_out
    # a.clock=0
    # a.save()
    print('time_out', time_out)
    return redirect('/empapp/home/')


def emp_home(request):
    u=request.user.id
    print(u)
    emp=request.user.emp.id
    current_date = datetime.now().date()
    print(current_date)
    at=attendance.objects.filter(emp=emp,date=current_date)
    # print(at)
    # for i in at:
    #     print(i.clock)
    # print(at)


    # at=attendance.objects.get(emp=u)
    # # print(at)
    # if request.method =='POST':
    #     user = request.user.emp.id
    #     print(user)
    #     t=request.POST['clockin']
    #     print(t,'sdasdsad')
    #     current_time = datetime.now().time()
    #     current_date = datetime.now().date()
    #     print(current_date)
    #     print(current_time)
    #     a = attendance(emp_id=user, timein=current_time, timeout='00:00', date=current_date)
    #     a.save()
    #     return render(request,'empapp/home.html',{'a':a,'t':t})

    return render(request,'empapp/home.html',{'at':at})
def emp_list(request):
    emps = Emp.objects.all().order_by('name')

    return render(request,'empapp/emp_list.html',{'emps':emps})

def profile(request):
    u=request.user.id
    emps=Emp.objects.get(user=u)
    print(emps)
    return render(request,'empapp/profile.html',{'emp':emps})

# def Attendance(request):
#     # print(True)
#     if request.method=='POST':
#         user=request.user.emp.id
#         print(user)
#
#
#         t=request.POST['timein']
#         print(t,'''tttt''')
#         if t=='True':
#         #     print(True,'ttttttt')
#         #     t = request.POST['timein']
#             current_time = datetime.now().time()
#             current_date = datetime.now().date()
#             print(current_date)
#             print(current_time)
#             a=attendance(emp_id=user,timein=current_time,timeout='00:00',date=current_date)
#             a.save()
#             print('a',a)
#             return render(request, 'empapp/home.html', {'a': a,'t':t})
#         else :
#
#             # t = request.POST['timeout']
#             current_date = datetime.now().date()
#             print(current_date)
#             print('sds',True)
#             time_out = datetime.now().time()
#             a = attendance.objects.filter(emp_id=user,date=current_date).update(timeout=time_out)
#             print('time_out',time_out)
#             return render(request, 'empapp/home.html', {'time_out': time_out})
#             # a.timeout=time_out
#
#         # current_time = datetime.now().strftime('%H:%M:%S')
#
#
#         # print(time.asctime(time.localtime(time.time())))
#         # return redirect('/')
#     else:
#         pass
#     return render(request,'empapp/home.html')
#

def Leave(request):
    if request.method =='POST':
        user = request.user.id
        print(user)

        reason=request.POST['reason']
        type=request.POST['type']
        date=request.POST['date']
        hours=request.POST['hours']
        print(user,reason,type,date,hours)
        l=leave(user_id=user,reason=reason,date=date,type=type,hours=hours)
        l.save()
        print(l)
        messages.warning(request, " Leave is applied ")
        return redirect('/empapp/home/')
    return render(request,'empapp/leave.html')


def profileupdate(request):
    user = request.user.id
    p=Emp.objects.filter(user=user)
    print(p)
    return render(request,'empapp/profileupdate.html',{'p':p})

def updateprofile(request):
    user = request.user.id
    if request.method == 'POST':
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        skill=request.POST['skill']
        print(skill)
        img1=request.FILES.get('image')
        print(img1)
        if img1 != None:
            print('img1', img1)
            fss = FileSystemStorage()
            file = fss.save(img1.name, img1)
            file_url = fss.url(file)
            print('f', file_url)
            p = Emp.objects.filter(user=user).update(name=name,phone=phone,address=address,image=img1,skill=skill)
        else:
            p = Emp.objects.filter(user=user).update(name=name, phone=phone, address=address,skill=skill)



        return redirect('/empapp/profile/')
    else:
        pass
    return render(request,'empapp/profileupdate.html')





def leavelist(request):
    user=request.user.id
    l=leave.objects.filter(user_id=user).order_by('-id')
    return render(request,'empapp/leavelist.html',{'l':l})