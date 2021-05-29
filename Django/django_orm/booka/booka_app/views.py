from django.shortcuts import redirect, render, HttpResponse
from .models import Author,Book
def index(request):
    context={
        "book": Book.objects.all()
        

    }
    return render(request,"index.html",context)
def add_book(request):
    Book.objects.create(title=request.POST['title'],desc=request.POST['des'])
    return redirect("/")


def author(request):
    context = {
    "author": Author.objects.all(),
    }
    return render(request,"author.html",context)


def add_author(request):
    Author.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'])
    return redirect("/author")

# def author_det(request,x):
#     context={
#         "r":Author.objects.get(id=x),
#         "g": r.authors.all()
#     }
#     return render(request,"det.html",context)

def dis(request,id):
    context={
        'author_all':Author.objects.all(),
        'book_a':Book.objects.get(id=id)
    }
    return render(request,"det.html",context)



def a_b(request,id):
    
    book=Book.objects.get(id=id)
    authortoadd=Author.objects.get(id=request.POST['sc'])
    book.authors.add(authortoadd)
    id=str(id)
    return redirect('/books/'+id)

def dis1(request,id):
    context={
        'book_all':Book.objects.all(),
        'auth_a':Author.objects.get(id=id)
    }
    return render(request,"auth.html",context)

def ps(request,id):
    auth_1=Author.objects.get(id=id)
    auth= Book.objects.get(id=request.POST['scr'])
    auth_1.books.add(auth)

    id=str(id)
    return redirect("/authors/"+id)