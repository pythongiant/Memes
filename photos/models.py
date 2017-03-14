from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Memes(models.Model):
    
    joker=models.CharField(max_length=250)
    description=models.CharField(max_length=140)
    photo_link=models.CharField(max_length=10000)
    def __str__(self):
        return self.description+"-"+self.joker
        
class Comment(models.Model):
    name=models.CharField(max_length=100)
    Memetitle=models.CharField(max_length=140)
    comment=models.CharField(max_length=100,null=True)
   
    def __str__(self):
        return self.name+"-"+self.comment
