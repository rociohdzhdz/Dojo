from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import random
# Create your views here.
def index(request):
    #return HttpResponse("placeholder to later display a list of all blogs")
    return render(request,'index.html')
def new(request):
    #return HttpResponse("placeholder to display a new form to create a new blog")
    return render(request, "new.html")
def create(request):
    print("You created a new blog post")
    print(request.POST)
    print(request.POST ['pname'])
    print(request.POST ['bpost'])
    print(request.POST ['pemail'])
    request.session['blogpost']=request.POST['bpost']
    request.session['blogname']=request.POST['pname']
    request.session['blogmail']=request.POST['pemail']
    return redirect('/')

def show(request, number):
    #return HttpResponse(f'This is a placeholder to diaplay blog: {number}')
    context={  
        'blog_id':number,
        'time': strftime("%Y-%m-%d %H:%M %p", gmtime()),
        'randy': int(random.random()*100)
    }
    return render(request, "show.html", context)

def edit(request, number):
    return HttpResponse(f'This is a placeholder to edit blog: {number}')

def destroy(request, number):
    return HttpResponse(f'This is a placeholder to delete blog: {number}')