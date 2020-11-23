from django.shortcuts import render,redirect
from . forms import ImageUploadForm,ImageProfileForm,CommentForm
from .models import Image,Comments,Profile
from django.contrib.auth.decorators import login_required
from vote.managers import  VotableManager
from django.contrib.auth.models import User
votes = VotableManager()

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    return render(request, 'insta/index.html',{"images":images})

def about(request):
    return render(request, 'insta/about.html')


