from django.shortcuts import redirect, render, HttpResponse
from . models import Dojos,Ninjas
def root(request):
    context={
        "dojos" : Dojos.objects.all(),
        "ninjas" : Ninjas.objects.all(),
        
    }
    return render(request,"index.html",context)
def dj(request):
    Dojos.objects.create(name=request.POST['name'],city=request.POST['City'],state=request.POST['state'])
    return redirect("/")

def nj(request):
    print(request.POST['dojo'])
    Ninjas.objects.create(firstname=request.POST['fname'],lastname=request.POST['lname'],dojos_id=Dojos.objects.get(id=int(request.POST['dojo'])))
    return redirect("/")
     
def del1(request):
     Dojos.objects.get(id=int(request.POST['del'])).delete()
     return redirect("/")