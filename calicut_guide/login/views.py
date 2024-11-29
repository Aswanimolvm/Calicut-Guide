from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login

# Create your views here.
def login(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        PASSWORD = request.POST.get("PASSWORD")
        obj = Login.objects.filter(username=uname,password=PASSWORD)
        print(len(obj))
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.user_id
            if tp == "admin":
                request.session["user_id"] = uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp == "org":
                request.session["organisation_id"] = uid
                return HttpResponseRedirect('/temp/org/')


            objlist = "username or password incorrect...please try again...!"
            context = {
                'msg': objlist
            }
            return render(request,'login/login.html',context)
    return render(request,'login/login.html')
