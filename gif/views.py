from django.shortcuts import render,get_object_or_404,redirect
from .models import Gif,Comments
from .forms import PostForm
# Create your views here.
def index(request):
    return render(request,"gif/index.html",{})

def gifs(request):
    all_gifs=Gif.objects.all()
    return render(request,"gif/gif.html",{"gifs":all_gifs}) 

def detail(request,gif_id):
     gif=get_object_or_404(Gif,pk=gif_id)
     if request.method=="POST":
         form=PostForm(request.POST)
         if form.is_valid():
             comment=form.cleaned_data['comment']#add the data from the comment 
             name=form.cleaned_data['name']#add the name from the comment 
             meme_title=form.cleaned_data['meme_title']
             Thecomment=Comments.objects.create(name=name,comment=comment,Memetitle=meme_title)#make a new instance of the model
             Thecomment.save()
     else:
            form = PostForm()   
     All_comments=Comments.objects.all()            
     context={
        "name":gif.joker,
        "description":gif.description,
        "photo":gif.photo_link,
        "plus1":gif.id+1,
        "minus1":gif.id-1,
        "form":form,
        "comment":All_comments
    }
     return render(request,"gif/detail.html",context)

def PageRedirect(request):
    return redirect('/gif/'+str(Gif.objects.count()))
def PageMoreRedirect(request):
    return redirect('/gif/1')