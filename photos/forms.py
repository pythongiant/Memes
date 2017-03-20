from django import forms
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
#The comment Post Form 
class PostForm(forms.Form):
    comment = forms.CharField(label="your comment:",max_length=256)
#To add a User into the database    

class Add(forms.Form):
    Username=forms.CharField(label="Username:",initial=" ")
    Password=forms.CharField(widget = forms.PasswordInput(),initial="")
    
    Email=forms.EmailField(label="Email Id:",initial="")

#The Login Form, For Authentication    
class Authenticate(forms.Form):
    
    Username=forms.CharField(label="Username:",initial=" ")
    Password=forms.CharField(widget = forms.PasswordInput(),initial="") 

#the form which enables users to add their own memes
class UserMeme(forms.Form):
    title=forms.CharField(label="Title for your meme:",initial=" ")
    meme=forms.FileField(label="Choose your meme")
    
    