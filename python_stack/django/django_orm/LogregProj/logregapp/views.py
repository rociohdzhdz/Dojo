from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    #return HttpResponse('placeholder to users reg')
    return render(request, "index.html")

def registerus(request):
    if request.method == "POST":
        errors=User.objects.validator(request.POST)
        print(errors)
        if len(errors)>0:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/')
        new_user = User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['mail'],password=request.POST['pass'])
        request.session['usrname']=new_user.first_name
        return redirect('/success')
    return redirect ('/')

def loginus(request):
    if request.method == "POST":
        log_usr=User.objects.filter(email=request.POST['mail2'])
        print(User.objects.all())
        if len(log_usr) >0:
            log_usr = log_usr[0]
            if log_usr.password == request.POST['pass2']:
                request.session['usrname']=log_usr.first_name
                return redirect('/success')
    return redirect('/')

def success(request):
    if 'usrname' not in request.session:
        return redirect('/')
    return render(request,"success.html")

def logoutus(request):
    request.session.flush()
    return redirect('/')
