from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from org.models import Organisation
from login.models import Login

# Create your views here.
def post_org(request):
    obk=""
    if request.method=='POST':
        obj=Organisation()
        obj.user_name=request.POST.get('name')
        obj.address=request.POST.get('address')
        obj.location=request.POST.get('location')
        obj.phone_number=request.POST.get('mobilenumber')
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.id_proof = myfile.name
        # obj.id_proof=request.POST.get('choose file')
        obj.password=request.POST.get('password')
        obj.e_mail=request.POST.get('e-mail')
        obj.status='pending'
        obj.save()
        ob=Login()
        ob.username=obj.user_name
        ob.password=obj.password
        ob.type='org'
        ob.user_id=obj.organisation_id
        ob.save()
        obk="k"
    context={
        'msg':obk
    }
    return render(request,'org/org_reg.html', context)