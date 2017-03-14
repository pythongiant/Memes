#import our libraries
from .models import Memes,Comment#import the memes and the comments
from django.shortcuts import render,get_object_or_404,redirect#import some shortcuts
from .forms import PostForm,Add,Authenticate#import the form model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

#render the index page

def index(request):
    return render(request,"photos/index.html",{})
    
def detail(request,meme_id):
    #get the memes
     memes=get_object_or_404(Memes,pk=meme_id)

     if request.method=="POST":
         form=PostForm(request.POST)#populate
         if form.is_valid():
             comment=form.cleaned_data['comment']#add the data from the comment 
             name=request.user.username 
             meme_title=memes.description
             Thecomment=Comment.objects.create(name=name,comment=comment,Memetitle=meme_title)#make a new instance of the model
             Thecomment.save()
     else:
            form = PostForm()        
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
    context={"all_memes":all_memes}
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
                return redirect('/photos/')


def LoginForm(request):
    form=Authenticate()
    return render(request, 'photos/login.html', {'Login': form})

            
    


    