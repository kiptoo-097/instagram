from django.db import models 
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from vote.models import VoteModel
from cloudinary.models import CloudinaryField



class Image(VoteModel,models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=50)
    image_caption = models.CharField(max_length=50)
    likes = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    

