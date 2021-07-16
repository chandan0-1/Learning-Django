from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_Hello1(request):
  return HttpResponse("Hello from Server.....")

# Serving a static Html file
def say_Hello2(request):
  return render(request, "hello.html", {"name": "Chandan"})