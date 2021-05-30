from io import RawIOBase
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
                
                x=User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['email'],password=request.POST['password'],password1=request.POST['password1'])

                
                
                request.session['id']=x.id
                return redirect("/suc")
            else:
                return redirect("/")

def logout(request):
    del request.session['email']
    return redirect("/")


def suc(request):
    context={
    "book1":Book.objects.all(),
    "use":User.objects.get(id= request.session['id'])
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
                request.session['id']=user[0].id
                
                
                return redirect("/suc")
            return redirect("/")
        else:
            return redirect("/")
    else:
        
        
        
                    
        
        return HttpResponse("The Email or the Password is wrong")
    
def delete(request,id):

       x=User.objects.get(id=id)
       y=x.delete()
       return redirect("/")
def add_book(request):
    user=User.objects.get(id=request.session['id'])
    book=Book.objects.create(title=request.POST['title'],desc=request.POST['desc'],upload_by=user)
    user.liked_books.add(book)

    return redirect("/suc")
def add_fav(request,id):
    user=User.objects.get(id= request.session['id'])
    book=Book.objects.get(id=id)
    user.liked_books.add(book)
    return redirect("/suc")
def show(request,id):
    context={
        'user':User.objects.get(id=request.session['id']),
        'book':Book.objects.get(id=id)
    }
    return render(request,"show.html",context)
def delete1(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("/suc")
def update(request,id):
    book=Book.objects.get(id=id)
    book.title=request.POST['title']
    book.desc=request.POST['desc']
    book.save()

    return redirect("/suc")

def n_fav(request,id):
    user=User.objects.get(id= request.session['id'])
    book=Book.objects.get(id=id)
    user.liked_books.remove(book)
    return redirect("/suc")