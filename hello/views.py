from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello ,World")

def greet(request):
    return HttpResponse("Hello,Mrinaal")

def welcome(request,name):
    return HttpResponse("hello, "+name)

def html(request):
    return render(request,hello.html,{})
    