from django.shortcuts import render,redirect
from django.http  import HttpResponse

# Create your views here.
def home(request):
    images= Image.objects.all()
    return render(request, "home.html")
