from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from news.models import News
import datetime

# Create your views here.
def news(request):
    if request.method=='POST':
        obj=News()
        obj.news_title=request.POST.get('title')
        obj.news=request.POST.get('news')
        obj.location=request.POST.get('location')
        myfile=request.FILES['image']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.image=myfile.name
        # obj.image=request.POST.get('image')
        obj.date=datetime.datetime.today()
        obj.save()
    return render(request,'news/news.html')
def viewnews(request):
    ob=News.objects.all()
    context={
        'd':ob
    }
    return render(request,'news/viewnews.html',context)

def delete(request,idd):
    obj=News.objects.get(news_id=idd)
    obj.delete()
    return viewnews(request)

def vn(request):
    ob=News.objects.all()
    context={
        'd':ob
    }
    return render(request,'news/vv.html',context)
# def delete(request.id())