from django.shortcuts import redirect
def red(request):
    return redirect("/photos/login")
def index(request):
    return redirect("/photos")