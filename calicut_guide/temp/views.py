from django.shortcuts import render

# Create your views here.
def admin(request):
    return render(request,'temp/admin.html')

def home(request):
    return render(request,'temp/home.html')

def user(request):
    return render(request,'temp/user.html')

def org(request):
    return render(request,'temp/organisation.html')

def mhome(request):
    return render(request,'temp/main_home.html')

def public(request):
    return render(request,'temp/public_user.html')

