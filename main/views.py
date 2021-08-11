
from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    wizards = Wizard.objects.all()

    context = {
        'saludo': 'Hola',
        'wizards': wizards
    }
    return render(request, 'index.html', context)

def createwiz(request):
    
    name = request.POST['name']
    house = request.POST['house']
    pet = request.POST['pet']
    age = request.POST['age']
    new_wiz = Wizard.objects.create( name = name, house=house, pet=pet, year=age)
    return redirect("/")

def delwiz(request):
    wizid = request.POST['id']
    wizdel = Wizard.objects.get(id=wizid)
    wizdel.delete()

    return redirect("/")

def createninja(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    dojo = request.POST['dojo']
    new_ninja = Ninjas.objects.create(first_name = first_name, last_name = last_name, Dojo = Dojos.objects.get(id=dojo))

    return redirect("/dojos")

def ninjas (request):
    dojos = Dojos.objects.all()
    context = {
        'dojos' : dojos
    }
    return render(request, 'dojos.html',context)


def second(request, name):
    return HttpResponse('Hola ' + name)

