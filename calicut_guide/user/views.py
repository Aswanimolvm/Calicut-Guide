from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from user.models import User
from login.models import Login


# Create your views here.
def post_user(request):
    obk=""
    if request.method=='POST':
        obj=User()
        obj.user_name=request.POST.get('name')
        obj.age=request.POST.get('age')
        obj.gender=request.POST.get('gender')
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
        obk="k"
    context={
        'msg':obk
    }
    return render(request,'user/register.html', context)


# def view_registration(request):
#     ob=User.objects.all()
#     context={
#         'e':ob
#     }
#     return render(request, 'user/viewregistration.html',context)
#

