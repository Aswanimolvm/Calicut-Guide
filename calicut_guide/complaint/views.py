from django.shortcuts import render
from complaint.models import Complaint
from facility.models import Facility
import datetime
# Create your views here.
def complaint(request):
    if request.method=='POST':
        obj=Complaint()
        obj.complaint=request.POST.get('complaint')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.username=request.POST.get('un')
        obj.save()
    return render(request,'complaint/complaint.html')

# def post_replay(request,idd):
#     if request.method == 'POST':
#         obj = Complaint.objects.get(complaint_id=idd)
#         obj.reply =request.POST.get('replay')
#         obj.save()
#         return viewcomplaint(request)
#
#     return render(request,'complaint/post_replay.html')

def viewcomplaint(request):
    ob=Complaint.objects.all()
    context={
        'c':ob
    }
    return render(request,'complaint/viewcomplaint.html',context)


# def view_replay(request):
#     # ss= request.session["user_id"]
#     ob = Complaint.objects.all()
#     context = {
#         'r': ob
#     }
#     return render(request,'complaint/view_reply.html',context,)

