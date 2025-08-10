from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("home/",emp_home),
    path("add-emp/",add_emp),
    path("delete-emp/<int:emp_id>",delete_emp),
    path("viewprofile/<int:emp_id>",viewprofile),
    path("update-emp/<int:emp_id>",update_emp),
    path("do-update-emp/<int:emp_id>",do_update_emp),
    path('search/',search),
    path('leavelist/',leavelist),
    path('leaveapprove/<int:id>/',leaveapprove),
    path('leavereject/<int:id>/',leavereject),
    path("attendancedetail/", attendancedetail),
    path('login/',Login),
    path('logout/',Logout),

]
