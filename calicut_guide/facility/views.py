from django.shortcuts import render
from facility.models import Facility
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
import datetime

# Create your views here.
def facility(request):
    if request.method=='POST':
        obj=Facility()
        obj.facility_type=request.POST.get('facility')
        obj.organisation_id=1
        obj.location=request.POST.get('location')
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.image = myfile.name
        # obj.image=request.POST.get('image')
        obj.phone_number=request.POST.get('number')



        obj.user_id=1
        obj.save()

    return render(request,'faacility/facility.html')

def viewfacility(request):
    ob=Facility.objects.all()
    context={
        'a':ob
    }
    return render(request,'faacility/viewfacility.html',context)


def viewfacility_req(request):
    if request.method=='POST':
        vv=request.POST.get('search')
        sv=request.POST.get('loc')
        ob=Facility.objects.filter(Q(facility_type__icontains=vv) | Q(location__icontains=vv),details__status='working')
        context = {
            'a': ob
        }
        return render(request,'faacility/request_facility.html',context)
    else:
        ob=Facility.objects.all()
        context={
            'a':ob
        }
        return render(request, 'faacility/request_facility.html', context)

def public_vw(request):
    if request.method=='POST':
        vv=request.POST.get('search')
        sv=request.POST.get('loc')
        ob=Facility.objects.filter(Q(facility_type__icontains=vv) | Q(location__icontains=vv),details__status='working')
        context = {
            'a': ob
        }
        return render(request,'faacility/public_user.html',context)
    else:
        ob=Facility.objects.all()
        context={
            'a':ob
        }
        return render(request, 'faacility/public_user.html', context)


# def accept(request,idd):
#     ob=Facility.objects.get(facility_id=idd)
#     ob.status='accepted'
#     ob.save()
#     return viewfacility(request)
#
# def reject(request,idd):
#     ob=Facility.objects.get(facility_id=idd)
#     ob.status='rejected'
#     ob.save()
#     return viewfacility(request)

def manage(request):
    ob=Facility.objects.all()
    context={
        'a':ob
    }
    return render(request,'faacility/manage_fac.html',context)

def working(request,idd):
    obj=Facility.objects.get(facility_id=idd)
    obj.status='working'
    obj.save()
    return manage(request)

def closed(request,idd):
    obj=Facility.objects.get(facility_id=idd)
    obj.status='closed'
    obj.save()
    return manage(request)


