from django.db import models
from tinymce.models import HTMLField



class Picture(models.Model):
    image = models.ImageField(upload_to='images/')
    picture_name = models.CharField(max_length=50)
    picture_caption = models.CharField(max_length=50)
    likes = models.PositiveIntegerField(default=0)
    
    
    def save_picture(self):
        self.save()
        
    def delete_picture(self):
        self.delete()
        
    def __str__(self):
        
        return self.picture_name