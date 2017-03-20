from __future__ import unicode_literals
from time import time
from django.db import models

"""
Author:Srihari Unnikrishnan
Country:India,
City: New Delhi,
State:New Delhi,
Github Username : Pythongiant,
Framework:Django,
Language:Python,
Project Name: Meme Site
"""



#Meme Model
def get_upload_file_name(instance,filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'),filename)

class Memes(models.Model):
    
    joker=models.CharField(max_length=250)
    description=models.CharField(max_length=140)
    photo_link=models.FileField(upload_to=get_upload_file_name)
    def __str__(self):
        return self.description+"-"+self.joker

#the Comment Model        
class Comment(models.Model):
    name=models.CharField(max_length=100)
    Memetitle=models.CharField(max_length=140)
    comment=models.CharField(max_length=100,null=True)
   
    def __str__(self):
        return self.name+"-"+self.comment
