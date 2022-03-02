from django.shortcuts import render
from django.http import HttpResponse

import datetime

# Create your views here.

def hello1(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)


def hello2(request):
   return render(request, "myapp/hello.html", {})

def hello3(request):
   today = datetime.datetime.now().date()
   return render(request, "myapp/hello2.html", {"today" : today})

def hello4(request, number):
   text = "<h1>welcome to my app number %s!</h1>"% number
   return HttpResponse(text)