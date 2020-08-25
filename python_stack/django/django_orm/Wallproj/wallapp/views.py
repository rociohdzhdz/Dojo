from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from .models import User, wallMessage, Comment
import bcrypt

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
        
        pw_hash=bcrypt.hashpw(request.POST['pass'].encode(),bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['mail'],password=pw_hash)
        print(new_user.password)
        request.session['usrname']=new_user.first_name
        request.session['user_id']=new_user.id
        return redirect('/success')
    return redirect ('/')

def loginus(request):
    if request.method == "POST":
        log_usr=User.objects.filter(email=request.POST['mail2'])
        print(User.objects.all())
        if len(log_usr) >0:
            log_usr = log_usr[0]
            if bcrypt.checkpw(request.POST['password'].encode(), log_usr.password.encode()):
                request.session['usrname']=log_usr.first_name
                request.session['user_id']=log_usr.id
                return redirect('/success')
    return redirect('/')

def success(request):
    if 'usrname' not in request.session:
        return redirect('/')
    context={
        'all_messages':wallMessage.objects.all()
    }
    return render(request,"success.html",context)

#Wall Functionality
def createmessage(request):
    if request.method =="POST":
        errors = wallMessage.objects.validator(request.POST)
        if errors:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/success')
        new_message = wallMessage.objects.create(content=request.POST['content'], poster=User.objects.get(id=request.session['user_id']))
        print(new_message)
        return redirect('/success')
    return redirect('/')

def profile(request,id):
    context={
        'one_user':User.objects.get(id=id)
    }
    return render(request, "profile.html", context)

def edit(request,id):
    onemessage=wallMessage.objects.get(id=id)
    if request.method == "POST":
        onemessage.content=request.POST['content']
        onemessage.save()
        return redirect(f'/profile/{str(onemessage.poster.id)}')
    context={
        'editmess': onemessage
    }
    return render(request, "edit.html", context)

def delete(request,id):
    wallMessage.objects.get(id=id).delete()
    return redirect('/success')

def addcomment(request,id):
    poster=User.objects.get(id=request.session['user_id'])
    msg=wallMessage.objects.get(id=id)
    Comment.objects.create(content=request.POST['content'], poster=poster, message=msg)
    return redirect('/success')

def logoutus(request):
    request.session.flush()
    return redirect('/')
