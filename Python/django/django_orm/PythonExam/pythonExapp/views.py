from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import User, Quote
import bcrypt

# Create your views here.
def index(request):
    #return HttpResponse('placeholder to users reg')
    return render(request, "index.html")

def newuser(request):
    if request.method == "POST":
        errors=User.objects.validator(request.POST)
        print(errors)
        if len(errors)>0:
            for key, values in errors.items():
                messages.error(request,values)
            return redirect('/')
        pw_hash=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user_mail=User.objects.filter(email=request.POST['mail'])
        if len(new_user_mail)>0:
            return redirect('/userexist')
        new_user=User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['mail'],password=pw_hash)
        print(new_user)
        request.session['usrname']=new_user.first_name + " " + new_user.last_name
        request.session['usr_id']=new_user.id
        return redirect('/quotes')
    return redirect('/')

def usererror(request):
    return render(request,"ErrorUser.html")

def userexist(request):
    return render(request, "UserExist.html")

def errorprofile(request):
    return render(request, "errorprofile.html")

def quotes(request):
    if 'usrname' not in request.session:
        return redirect('/')
    context={
        'all_quotes':Quote.objects.all()
    }
    return render(request, "quotes.html", context)

def loginuser(request):
    if request.method == "POST":
        loggedusr=User.objects.filter(email=request.POST['logmail'])
        print(User.objects.all())
        if len(loggedusr)>0:
            loggedusr=loggedusr[0]
            if bcrypt.checkpw(request.POST['logpass'].encode(), loggedusr.password.encode()):
                request.session['usrname']=loggedusr.first_name +" " + loggedusr.last_name
                request.session['usr_id']=loggedusr.id
                return redirect('/quotes')
        return redirect('/usererror')
    return redirect('/')

def newquote(request):
    if request.method == "POST":
        #errors validation for quotes
        errors=Quote.objects.validator(request.POST)
        print(errors)
        if len(errors)>0:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/quotes')
        new_quote=Quote.objects.create(author=request.POST['author'],quotedes=request.POST['quotedes'],poster=User.objects.get(id=request.session['usr_id']))
        print(new_quote)
        return redirect('/quotes')
    return redirect('/')

def user(request,id):
    context={
        'oneuser':User.objects.get(id=id)
    }
    return render(request,"userprofile.html",context)

def myaccount(request,id):
    oneprofile=User.objects.get(id=id)
    if request.method == "POST":
        if request.POST['editfname'] == "" or request.POST['editlname'] == "" or request.POST['editmail']=="":
            return redirect('/errorprofile')
        oneprofile.first_name=request.POST['editfname']
        oneprofile.last_name=request.POST['editlname']
        oneprofile.email=request.POST['editmail']
        oneprofile.save()
        return redirect(f'/user/{str(oneprofile.id)}')
    context={
        'editprofile': oneprofile
    }
    return render(request, "EditMyAccount.html", context)

def givelike(request,id):
    liked_quote=Quote.objects.get(id=id)
    user_liked=User.objects.get(id=request.session['usr_id'])
    liked_quote.likes.add(user_liked)
    return redirect('/quotes')

def logout(request):
    request.session.flush()
    return redirect('/')

def delete(request,id):
    Quote.objects.get(id=id).delete()
    return redirect ('/quotes')