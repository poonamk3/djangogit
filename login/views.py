from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def methodinfo(request):  
    return HttpResponse("Hii request is:"+request.method)  