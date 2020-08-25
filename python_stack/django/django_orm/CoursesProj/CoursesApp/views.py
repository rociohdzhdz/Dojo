from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course
# Create your views here.
def index(request):
    #return HttpResponse("This is working")
    context={
        'all_courses':Course.objects.all()
    }
    return render(request,'index.html',context)

def create (request):
    if request.method =='POST':
        errors = Course.objects.validator(request.POST)
        print(errors)
        if len(errors) >0:
            for key, values in errors.items():
                messages.error(request,values)
            return redirect('/')
        print(request.POST)
        Course.objects.create(name=request.POST['name'],description=request.POST['desc'])
        return redirect('/')
    return redirect('/')

def onecourse(request,id):
    context={
        'one_course': Course.objects.get(id=id)
    }
    return render(request,"oneCourse.html",context)

def remove(request,id):
    #return HttpResponse("To remove")
    to_delete=Course.objects.get(id=id)
    to_delete.delete()
    return redirect('/')