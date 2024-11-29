from django.shortcuts import render
from request.models import Request
from facility.models import Facility
import datetime

# Create your views here.
def request(request,idd):
    ss = request.session["user_id"]
    if request.method=='POST':
        obj=Request()
        obj.request=request.POST.get('request')
        obj.location='pending'
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.facility_id=idd
        obj.user_id=ss
        obj.status='pending'
        obj.save()
    return render(request,'request/request.html')
def view_request(request):
    ob=Request.objects.all()
    context={
        'e':ob
    }
    return render(request, 'request/viewrequest.html',context)
def accept(request,idd):
    ob=Request.objects.get(request_id=idd)
    ob.status='accepted'
    ob.save()
    return view_request(request)


