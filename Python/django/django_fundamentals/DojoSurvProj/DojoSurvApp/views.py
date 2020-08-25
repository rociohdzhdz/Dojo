from django.shortcuts import render, redirect
import random, datetime

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
        request.session['messages'] = []
    context = {'gold': request.session['gold'], 'messages': request.session['messages']}
    return render(request, 'ninja_app/index.html', context)

def processM(request):
    if request.method == "POST":
        directory = {'farm': [10,20],'cave': [5,10],'house': [2,5],'casino': [-50,50]}
        now = datetime.datetime.now()

        for key in directory:
            if key == request.POST['location']:
                temp = random.randint(directory[key][0], directory[key][1])
                request.session['gold'] += temp
                if temp >= 0:
                    request.session['messages'].insert(0,'Earned '+ str(temp) + ' golds from the ' + key + '! ('+now.strftime("%Y/%m/%d %I:%M %p")+')')
                else:
                    request.session['messages'].insert(0,'Entered a ' + key + ' and lost '+ str(temp*-1) + ' golds... Ouch.. ('+now.strftime("%Y/%m/%d %I:%M %p")+')')
    return redirect("/")

def destroy(request):
    request.session.clear()
    return redirect("/")