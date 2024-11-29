from django.shortcuts import render
from feedback.models import Feedback
from facility.models import Facility
import datetime

# Create your views here.
def feedback(request):
    if request.method=='POST':
        obj=Feedback()
        obj.feedback=request.POST.get('feedback')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.username=request.POST.get('un')
        obj.save()
    return render(request,'feedback/feedback.html')


def viewfeedback(request):
    ob=Feedback.objects.all()
    context={
        'b':ob
    }
    return render(request,'feedback/viewfeedback.html',context)
