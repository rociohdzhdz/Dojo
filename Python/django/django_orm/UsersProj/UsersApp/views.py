from django.shortcuts import render, HttpResponse, redirect
from .models import Users
# Create your views here.
def index(request):
    #return render(request, "index.html")
    context={
        "all_users": Users.objects.all()
    }
    return render(request,"index.html",context)

def create(request):
    if request.method == 'POST':
        new_user= Users.objects.create(first_name=request.POST['fName'],last_name=request.POST['lName'],email_address=request.POST['mail'],age=request.POST['age'] )
        print(new_user)
        request.session['fName']=new_user.first_name
        request.session['id']=new_user.id
        request.session['lName']=new_user.last_name
        request.session['mail']=new_user.email_address
        request.session['age']=new_user.age 
    return redirect('/')