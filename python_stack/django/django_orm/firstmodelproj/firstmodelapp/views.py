from django.shortcuts import render, redirect, HttpResponse
from .models import Movie

# Create your views here.
def index(request):
    #return HttpResponse("placeholder to later display a list of all blogs")
    context={
        "all movies": Movie.objects.all()
    }
    return render (request, "index.html",context)