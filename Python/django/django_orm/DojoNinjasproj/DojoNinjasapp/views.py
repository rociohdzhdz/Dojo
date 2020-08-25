from django.shortcuts import render, HttpResponse, redirect
from .models import Dojos
from .models import Ninjas

# Create your views here.
def index(request):
    #return HttpResponse("placeholder to later display something")
    # context={
    #     "all movies": Movie.objects.all()
    # }
    # return render (request, "index.html",context)
    context={
        "all_dojos": Dojos.objects.all()
    }
    return render(request,"index.html",context)

def newdojo(request):
    if request.method == 'POST':
        new_dojo= Dojos.objects.create(name=request.POST['dname'],city=request.POST['dcity'],state=request.POST['dstate'],desc=request.POST['desc'] )
        """ print(new_dojo)
        request.session['dname']=new_dojo.name
        request.session['dcity']=new_dojo.city
        request.session['dstate']=new_dojo.state
        request.session['ddesc']=new_dojo.desc """
    return redirect('/')

def newninja(request):
    if request.method=='POST':
        new_ninja=Ninjas.objects.create(first_name=request.POST['nname'],last_name=request.POST['nlastname'],dojonam=Dojos.objects.get(id=request.POST['dojon']))
        """ print(new_ninja)
        request.session['nname']=new_ninja.first_name
        request.session['nlastname']=new_ninja.last_name
        request.session['ndname']=new_dojo.name """
    return redirect('/')