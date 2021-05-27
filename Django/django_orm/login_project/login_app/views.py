from django.shortcuts import redirect, render, HttpResponse
from .models import *
from django.contrib import messages
def index(request):
    context={
        "user1":User.objects.all(),
        "user2": User.objects.last()
    }
        
    
    return render(request,"index.html",context)
def cr(request):
        errors = User.objects.basic_validator(request.POST)
        
        if len(errors) > 0:
            
            for key, value in errors.items():
                messages.error(request, value)
            
            return redirect("/")
        else:
            request.session['email']=request.POST['email']
            if request.POST['password'] == request.POST['password1'] and request.session['email']==request.POST['email']:
                
                User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['email'],password=request.POST['password'],password1=request.POST['password1'])

                x = User.objects.last()
                id=str(x.id)
                return redirect("/suc/"+id)
            else:
                return redirect("/")

def logout(request):
    del request.session['email']
    return redirect("/")


def suc(request,id):
    context={
        "email":request.session['email'],
        'id':id
    }
    return render(request,"suc.html",context)
def login(request):
     

    user= User.objects.filter(email=request.POST['email1'])
    user1= request.POST['password2']
    id = user[0].id 
    if user1==user[0].password:
        
        if user:
            if user1==user[0].password:
                request.session['email']=user[0].email
                return redirect("/suc/" + str(id))
            return redirect("/")
        else:
            return redirect("/")
    else:
        
        
        
                    
        
        return HttpResponse("The Email or the Password is wrong")
    
def delete(request,id):

       x=User.objects.get(id=id)
       y=x.delete()
       return redirect("/")
