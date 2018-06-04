from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from permission_rbac.models import User
from permission_rbac.server.perssions import initial_session

def login(request):
    if request.method=="POST":
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")

        user=User.objects.filter(name=user,pwd=pwd).first()
        if user:
            request.session["user_id"]=user.pk
            # 注册权限到session中
            initial_session(user,request)

            return redirect('/stark/app01/customer/')


    return render(request,"login.html")