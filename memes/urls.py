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
from django.conf.urls import include,url
from django.contrib import admin
from . import account_redirect
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^gif/',include("gif.urls")),
    url(r'^photos/',include("photos.urls")),
    url(r'^accounts/login/',account_redirect.red),
]
