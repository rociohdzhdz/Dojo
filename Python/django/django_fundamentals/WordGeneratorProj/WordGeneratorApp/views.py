from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    #return HttpResponse("placeholder to later display a list of all blogs")
    return render(request,'index.html')


def show(request):
    if "rw_count" not in request.session.keys():
        print ("0")
        request.session['rw_count'] = 0
    else:
        print (" 1")
        request.session['rw_count'] += 1
    context = {
        "rw_count": request.session['rw_count'],
        "random_str": get_random_string(length=14)
    }
    return render(request,'index.html', context)

def reset(request):
    request.session['count'] = 0
    return redirect('/')