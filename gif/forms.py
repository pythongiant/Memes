from django import forms
 
class PostForm(forms.Form):
    comment = forms.CharField(label="your comment:",max_length=256)
    name=forms.CharField(label="name:",max_length=100)
    
    meme_title=forms.CharField(label="What is the title for the GIF")