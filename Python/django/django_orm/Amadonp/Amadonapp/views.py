from django.shortcuts import render, HttpResponse,redirect
from .models import Order, Product
from django.db.models import Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "index.html", context)

def checkout(request):
    last=Order.objects.last()
    price=last.total_price
    full_order = Order.objects.aggregate(Sum('quantity_ordered'))['quantity_ordered__sum']
    full_price = Order.objects.aggregate(Sum('total_price'))['total_price__sum']
    context = {
        'orders':full_order,
        'total':full_price,
        'bill':price,
    }
    return render(request, "checkout.html",context)

def buy(request):
    if request.method =='POST':
        quantity_from_form = int(request.POST['quantity'])
        price_from_form = float(request.POST['price'])
        total_charge = quantity_from_form * price_from_form
        print(request.POST)
        print("Charging credit card...")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        return redirect('/checkout')
    return redirect('/')