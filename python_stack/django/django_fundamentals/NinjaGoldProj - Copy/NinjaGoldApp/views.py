from django.shortcuts import render, HttpResponse, redirect
import random
# Create your views here.
def index(request):
    #return HttpResponse("working")
    return render(request, 'index.html')

def farm(request):
    request.session['earned_gold'] = random.randint(10, 20)
    #return render(request, "index.html")
    request.session['activityLog'].append(f"Won {earned_gold}") 