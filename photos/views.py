"""
Author:Srihari Unnikrishnan
Country:India,
City: New Delhi,
State:New Delhi,
Github Username : Pythongiant,
Framework:Django,
Language:Python,
Project Name: Meme Site
We most probably handle all the forms in the same way so hust to clarify stuff I wrote comments in the first form handel
"""
#import our libraries
from .models import *#import the memes and the comments
from django.shortcuts import render,get_object_or_404,redirect#import some shortcuts
from .forms import * #import the form model
from django.contrib.auth.models import User #Import the User module
from django.contrib.auth import authenticate,login,logout#import some more stuff
from django.contrib.auth.decorators import login_required
#render the index page

def index(request):
    return render(request,"photos/index.html",{})
 
def detail(request,meme_id):
    #get the memes
     memes=get_object_or_404(Memes,pk=meme_id)
     #check if the request made is POST
     if request.method=="POST":
         
         form=PostForm(request.POST)#populate
         #Check if the form is valid
         if form.is_valid():
             #fill data into the model and the form
             comment=form.cleaned_data['comment']#add the data from the comment 
             name=request.user.username 
             meme_title=memes.description
             Comment.objects.create(name=name,comment=comment,Memetitle=meme_title)#make a new instance of the model
             
     else:
            #Since it is a GET request populate it with empty Data
            form = PostForm()
     #get all the data for further processing in the renderd HTML file                    
     All_comments=Comment.objects.all()
#the contexts, pretty straightforward
     context={
         "name":memes.joker,
         "description":memes.description,
         "photo":memes.photo_link,
         "plus1":memes.id+1,
         "minus1":memes.id-1,
         "meme_id":meme_id,
         "form":form,
         "comment":All_comments,
         "hi":request.user.username
         }
   
     return render(request,"photos/detail.html",context)
         
#redirect
def PageRedirect(request):
    return redirect('/photos/'+str(Memes.objects.count()))

#redirect
def PageMoreRedirect(request):
    return redirect('/photos/1')

#context for the main meme page
def memesPage(request):
    all_memes=Memes.objects.all()
    context={"all_memes":all_memes,"hi":request.user.username}
    return render(request,"photos/meme.html",context)  
     
def AddUserForm(request):
    form = Add()
    return render(request, 'photos/add.html', {'Login': form})

def AddUser(request):
    if request.method == 'POST':
        form = Add(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            email=form.cleaned_data['Email']
            
            user = User.objects.create_user(username, email, password)
            
    return redirect("/photos/login")              

def AuthenticateUser(request):
    if request.method == 'POST':
        form = Authenticate(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            user=authenticate(username=username,password=password)        
            if user is not None:
                login(request,user)
                return redirect('/photos/memes.html')
            else:
                return render(request,"photos/invalid.html",{})

def LoginForm(request):
    form=Authenticate()
    return render(request, 'photos/login.html', {'Login': form})      

#The following functions allow users to post their own memes

def YourMeme(request):
    form=UserMeme()
    if request.method == 'POST':
        form = UserMeme(request.POST, request.FILES)
        if form.is_valid():
            meme =request.FILES["meme"]
            joker=request.user.username
            description=request.POST["title"]
            Memes.objects.create(joker=joker,photo_link=meme,description=description)
            return redirect("/photos/memes.html/")
    else:
        form = UserMeme()

    return render(request,'photos/usermeme.html',{'form':form,'hi':request.user.username})
    
def logoutUser(request):
    logout(request)
    return redirect("/photos/login/")

def PageFRedirect(request):
    return redirect("/photos/36")