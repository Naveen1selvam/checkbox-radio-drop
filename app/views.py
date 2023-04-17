from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Insertion of Topic is done successfully')

    return render(request,'insert_topic.html')
def insert_webpage(request):
        LTO=Topic.objects.all()
        d={'topic':LTO}
        if request.method=='POST':
            topic=request.POST['topic']
            n=request.POST['n']
            u=request.POST['u']
            e=request.POST['e']
            TO=Topic.objects.get(topic_name=topic)
            WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
            WO.save()
            return HttpResponse('Insertion of Webpage is done successfully')
        return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    LAO=Webpage.objects.all()
    d={'access':LAO}
    if request.method=='POST':
        names=request.POST['names']
        a=request.POST['a']
        d=request.POST['d']
        
        WO=Webpage.objects.get(name=names)
        
        AO=Accessrecord.objects.get_or_create(name=WO,author=a,date=d)[0]
        AO.save()
        return HttpResponse('Insertion of Accessrecord is done successfully')
    return render(request,'insert_accessrecord.html',d)

def retrieve_data(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        webqueryset=Webpage.objects.none()

        for i in td:
            webqueryset=webqueryset|Webpage.objects.filter(topic_name=i)
        d1={'webpages':webqueryset}
        return render(request,'display_webpage.html',d1)
    return render(request,'retrieve_data.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    return render(request,'checkbox.html',d)

def radio(request):

    LTO=Topic.objects.all()
    d={'topics':LTO}
    return render(request,'radio.html',d)