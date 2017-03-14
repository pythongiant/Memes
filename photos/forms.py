from django import forms

 
class PostForm(forms.Form):
    comment = forms.CharField(label="your comment:",max_length=256)
    
class Add(forms.Form):
    Username=forms.CharField(label="Username:",initial="your name")
    Password=forms.CharField(widget = forms.PasswordInput(),initial="")
    Email=forms.EmailField(label="Email Id:",initial="")
class Authenticate(forms.Form):
    Username=forms.CharField(label="Username:",initial="your name")
    Password=forms.CharField(widget = forms.PasswordInput(),initial="") 