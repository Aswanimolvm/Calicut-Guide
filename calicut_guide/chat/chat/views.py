from django.shortcuts import render
from user.models import User
from chat.models import Chat
import datetime
from django.db.models import Q
from nursery.models import Nursery
# Create your views here.
from login.models import Login


def con(request):
    ob= Nursery.objects.all()
    context={
        'u':ob
    }
    return render(request,'chat/viewcon.html',context)

def cochat(request,idd):
    ss=request.session["u_id"]
    obj = Nursery.objects.get(n_id=idd)
    ob = Chat.objects.filter(Q(user_id=ss) & Q(n_id=idd))
    context = {
        'kk': ob,
        'uu': obj,
    }
    if request.method == 'POST':
        obk = Chat()
        obk.message = request.POST.get('mssg')
        obk.n_id=idd
        obk.user_id=ss
        obk.rectype="nursery"
        obk.sendertype = "user"
        obk.save()
    return render(request, 'chat/chatuser1.html',context)



def std(request):
    ob=User.objects.all()
    context={
        'u':ob
    }
    return render(request,'chat/view user.html',context)


def stchat(request,idd):
    ss = request.session["u_id"]
    obj =User.objects.get(user_id=idd)
    ob=Chat.objects.filter(Q(user_id=idd) & Q(n_id=ss))
    context={
        'kk':ob,
        'uu':obj,
    }

    if request.method=='POST':
        obk=Chat()
        obk.message=request.POST.get('mssg')
        obk.user_id=idd
        obk.n_id=ss
        obk.rectype="user"
        obk.sendertype="nursery"
        obk.save()
    return render(request, 'chat/chatuser2.html',context)
