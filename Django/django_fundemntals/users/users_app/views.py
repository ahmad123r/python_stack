from django.shortcuts import redirect, render, HttpResponse
# other imports
from .models import users
# show all of the data from a table
def index(request):
    context = {
        "users" : users.objects.all()

    	
    }
    return render(request, "index.html", context)

def pro(request):
    users.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email_address=request.POST['email'],age=request.POST['age'])
    return redirect("/")
