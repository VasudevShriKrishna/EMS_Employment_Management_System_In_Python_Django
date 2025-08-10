from django.urls import path,include
from .views import *

urlpatterns = [
    path("home/",emp_home),
    path("emplist/",emp_list),
    path("profile/",profile),
    # path("attendance/",Attendance),
    path("clockin/",clockin),
    path("clockout/",clockout),
    path("profileupdate/",profileupdate),
    path("updateprofile/",updateprofile),
    path("leave/",Leave),
    path("leavelist/",leavelist),

    ]
