from django.contrib import admin
from .models import *
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
# Register your models here.
admin.site.register(Memes)
admin.site.register(Comment)
