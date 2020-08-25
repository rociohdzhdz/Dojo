from django.shortcuts import render, HttpResponse, redirect
from .models import Book
from .models import Publisher
# Create your views here.
def index(request):
    #return HttpResponse("placeholder to later display something")
    context={
        "all_books": Book.objects.all()
    }
    return render(request,"index.html",context)

def createbooks(request):
    if request.method == 'POST':
        new_book=Book.objects.create(title=request.POST['title'],desc=request.POST['description']) 
        print(new_book)
        request.session['title']=new_book.title
        request.session['id']=new_book.id   
        request.session['description']=new_book.desc
    return redirect('/')

def one_book(request, id):
    context={
        'one_book': Book.objects.get(id=id),
        'all_publishers': Publisher.objects.all()
    }
    return render(request,"oneBook.html", context)