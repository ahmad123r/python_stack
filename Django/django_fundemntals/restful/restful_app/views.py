from typing import ContextManager
from django.http import request
from django.shortcuts import redirect, render, HttpResponse
from .models import *
def index(request): 
    context={
        "r":Shows.objects.all()
    }
    return render(request,"index.html",context)

def new(request):
    
    return render(request,"new.html")


def create(request):
    if request.method == "POST":
        Shows.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            desc=request.POST['decs'],
            release_date=request.POST['rd']
        )
        x=Shows.objects.last()
        id=str(x.id)
    return redirect("/show/"+id)
def show(request,id):
    x=Shows.objects.get(id=id)
    
    context={
        'x':x
    }
    return render(request,"show.html",context)

def delete(request,id):
    x=Shows.objects.get(id=id)
    
    x.delete()
    return redirect("/")

def edit(request,id):
    context={
        "id":id,
        "x":Shows.objects.get(id=id)
    }

    return render(request,"edit.html",context)
    

def update(request,id):
    x=str(id)
    c=Shows.objects.get(id=id)
    c.title =request.POST['title']
    c.network =request.POST['network']
    c.release_date =request.POST['rd']
    c.desc=request.POST['desc']
    c.save()

  
    

    return redirect("/show/" + x)