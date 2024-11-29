from django.shortcuts import render
from details.models import Details
from django.core.files.storage import FileSystemStorage
from facility.models import Facility

def details(request,idd):
    obj=Facility.objects.get(facility_id=idd)
    context={
        'a':obj
    }
    if request.method=='POST':
        obj=Details()
        obj.address=request.POST.get('address')
        obj.location=request.POST.get('location')
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.image = myfile.name
        obj.website_link=request.POST.get('website')
        obj.phone_number=request.POST.get('number')
        obj.details=request.POST.get('details')
        obj.status='pending'
        obj.facility_id=idd
        # obj.chat=request.POST.get('chat')
        obj.save()
    return render(request,'details/details.html',context)


def  view_details(request):
    ob=Details.objects.all()
    context={
        'b': ob
    }
    return render(request,'details/view_details.html',context)

def view_detail_org(request):
     ob=Details.objects.all()
     context={
         'a':ob
     }
     return render(request,'details/view_details_org.html',context)

