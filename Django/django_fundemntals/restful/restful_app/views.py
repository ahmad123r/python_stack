from typing import ContextManager
from django.http import request
from django.shortcuts import redirect, render, HttpResponse
from .models import *
from django.contrib import messages
def index(request): 
    context={
        "r":Shows.objects.all()
    }
    return render(request,"index.html",context)

def new(request):
    
    return render(request,"new.html")


def create(request):
 

         # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Shows.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/new')
    else:
        messages.success(request, "Blog successfully updated")
    if request.method == "POST":
        Shows.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            desc=request.POST['desc'],
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
             # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Shows.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/new')
    else:
        messages.success(request, "Blog successfully updated")
    x=str(id)
    c=Shows.objects.get(id=id)
    c.title =request.POST['title']
    c.network =request.POST['network']
    c.release_date =request.POST['rd']
    c.desc=request.POST['desc']
    c.save()

  
    

    return redirect("/show/" + x)


