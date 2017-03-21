from django.conf.urls import url
from . import views
from .models import Memes
from django.conf import settings
from django.conf.urls.static import static

"""
Author:Srihari Unnikrishnan
Country:India,
City: New Delhi,
State:New Delhi,
Github Username : Pythongiant,
Framework:Django,
Language:Python,
Project Name: Meme Site,
Note:Action Url is actually the 'void' where the view uses the data from mostly a form
Note:Form Url is actually the 'void' where the view renders the form to HTML
"""

urlpatterns=[
    url(r'^$',views.index,name="index"),
    #photos/memes
    url(r'^memes',views.memesPage,name="memes_home"),
    #photos/memes/0(redirects to photos/memes/Memes.objects.count()+1)
    url(r'^0',views.PageRedirect,name="redirect"),
   
    #photos/number of memes+1 (redirects to photos/1)
    url(r'^'+str(Memes.objects.count()+1),views.PageMoreRedirect,name="more_redirect"),
    #photos/memes/meme_id[Decimals]
    url(r'^(?P<meme_id>[0-9]+)/$',views.detail,name="meme_detail"),
    #Action Url when you add a new Person to the databse's Username and Password
    url(r'^Add',views.AddUser,name="add"),
    #Form Url for adding a user 
    url(r'^add_me',views.AddUserForm,name="adduser"),
    #form url for logging a user in 
    url(r'^login',views.LoginForm,name="login"),
    #authorise the login(Action Url)
    url(r'^auth',views.AuthenticateUser,name="auth"),
    #Form Url for user to upload a meme
    url(r'^addmeme',views.YourMeme),
    #logout User
    url(r'^logout',views.logoutUser,name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
