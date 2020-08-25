from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from .models import Show

# Create your views here.
def index(request):
    return render(request,"index.html")
def shows(request):
    #return HttpResponse("placeholder to later display all shows") 
    context={
        'all_shows':Show.objects.all()
    }
    return render(request,'allShows.html',context)

def newshow(request):
    #return HttpResponse("placeholder to later display new show")
    return render(request,"newshow.html")

def createshow(request):
    #return HttpResponse("placeholder to later display all shows") 
    if request.method =='POST':
        errors = Show.objects.validator(request.POST)
        print(errors)
        if len(errors) >0:
            for key, values in errors.items():
                messages.error(request,values)
            return redirect('/shows/newshow')

        print(request.POST)
        Show.objects.create(title=request.POST['title'],network=request.POST['network'],releasedate=request.POST['released'],description=request.POST['desc'])
        return redirect('/shows/newshow')
    return redirect('/')

def one_show(request, id):
    #return HttpResponse("placeholder to later display one show")
    context={
        'one_show': Show.objects.get(id=id)
    }
    return render(request,"oneShow.html",context)

def editshow(request,id):
    one_show=Show.objects.get(id=id)
    context={
        'show':one_show
    }
    return render(request,'edit.html',context)

def updateshow(request,id):
    errors = Show.objects.validator(request.POST)
    print(errors)
    if len(errors) >0:
        for key, values in errors.items():
            messages.error(request,values)
            return render(request,'edit.html')
    to_update=Show.objects.get(id=id)
    to_update.title=request.POST['title']
    to_update.network=request.POST['network']
    to_update.releasedate=request.POST['released']
    to_update.description=request.POST['desc']
    to_update.save()
    return redirect ('/shows')

def destroyshow(request,id):
    to_delete=Show.objects.get(id=id)
    to_delete.delete()
    return redirect('/shows')
    