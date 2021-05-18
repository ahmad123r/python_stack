from django.shortcuts import render,redirect

from django.shortcuts import HttpResponse, redirect # add redirect to import statement
from django.http import JsonResponse
def root_method(request):
    return HttpResponse("String response from root_method")
def another_method(request):
    return redirect("/blog")
def redirected_method(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})